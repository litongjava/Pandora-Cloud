from src.pandora_cloud.server import ChatBot

if __name__ == "__main__":
    chat_bot = ChatBot(proxy=None, debug=True)
    port = "8018"
    print("http://127.0.0.1:%s" % port)
    chat_bot.run(bind_str=("0.0.0.0:%s" % port))

