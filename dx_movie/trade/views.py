from django.shortcuts import render
from rest_framework import viewsets
from .models import Card, Order
from .serializers import CardSerializer, OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.errors import TradeError, UserError
from utils.common import get_random_code
from utils.alipay import AliPay
from django.utils import timezone
from datetime import datetime
from account.models import Profile



# Create your views here.
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class AlipayAPIView(APIView):
    def get(self, request):
        """
        发起支付宝支付,有2种场景
        1.创建新支付
        2.支付未完成的订单
        """
        # 检测卡号id是否正确
        card_id = request.GET.get("card_id" , None)
        card = Card.objects.get(id=card_id)
        if not card:
            return Response(*TradeError.CardParamError)
        # 判断订单号是否存在，存在则表示执行之前未支付的订单
        # 否则，支付新订单
        order_sn = request.POST.get("order_sn" , None)
        try:
            order = Order.objects.get(order_sn=order_sn)
            out_trade_no = order.order_sn
        except:
            # 生成新的订单号
            out_trade_no = "pay" + datetime.now().strftime("%Y%m%d%H%M%S") + get_random_code(4)
            try:
                # 生成订单
                # uid = request.session.get('uid')
                uid = 'KDMq56nRWJL6jWUhLyQ7SC'
                Order.objects.create(
                    user = Profile.objects.get(pk=uid),
                    order_sn = out_trade_no,
                    order_mount = card.card_price,
                    card = card,
                    pay_time = timezone.now()
                )
            except Exception as e:
                print(e)
        try:
            alipay = AliPay()
            url = alipay.trade_page(out_trade_no, str(card.card_price), card.card_name, "支付宝测试", "FAST_INSTANT_TRADE_PAY")
            # return Response({"url": url})
            return Response(url)
        except Exception as e:
            print(e)
            return Response('支付失败')


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer