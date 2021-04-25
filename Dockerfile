# 任意のイメージを取得
FROM python

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# bs4が本体。
# lxmlはbs4をインストールするために必要。
# requestsは対象のWebページに接続するために使用。
RUN pip install requests lxml bs4 

WORKDIR /app

COPY app /app
COPY start.sh /start.sh

RUN chmod 755 /start.sh

RUN python --version

CMD [ "/start.sh" ]
