import os
import logging
import boto3
import json
import pandas as pd
import re
import base64
import requests

"""
#試験用
logger = logging.getLogger()
logger.setLevel(logging.INFO)
s3 = boto3.client('s3')
def lambda_handler(event, context):
    #line_uranai_1.json
    bucket = 'lineuranaibucket' # バケット名
    key = 'line_uranai_1.json'
    obj = s3.get_object(Bucket=bucket, Key=key)
    text = obj['Body'].read()
    zodiac_data_1 = json.loads(text.decode('utf-8'))
    
    #line_uranai_2.json
    bucket = 'lineuranaibucket' # バケット名
    key = 'line_uranai_2.json'
    obj = s3.get_object(Bucket=bucket, Key=key)
    text = obj['Body'].read()
    zodiac_data_2 = json.loads(text.decode('utf-8'))

    #pandasに置き換える
    df_1 = pd.DataFrame(zodiac_data_1, columns=['zodiac', 'rank', 'link'])
    df_2 = pd.DataFrame(zodiac_data_2, columns=['zodiac', 'rank', 'link'])
    df = pd.concat([df_1, df_2])
    dfs = {}
    for zodiac in df_1['zodiac']:
        df_1_temp = df_1[df_1['zodiac'] == zodiac]
        df_2_temp = df_2[df_2['zodiac'] == zodiac]
        df_combined = pd.concat([df_1_temp, df_2_temp])
        df_combined_sorted = df_combined.sort_values(by='rank')
        dfs[zodiac] = df_combined_sorted


    # ログに出力
    for zodiac, df in dfs.items():
        logger.info(f"Zodiac: {zodiac}\n{df}\n")

    return {
        "statusCode": 200,
        "body": "Processed data successfully" # 適切な応答メッセージを返す
    }    



"""


# 辞書を作成する
zodiac_dict = {
    '牡牛座': 'おうし座',
    '魚座': 'うお座',
    '山羊座': 'やぎ座',
    '蠍座': 'さそり座',
    '乙女座': 'おとめ座',
    '蟹座': 'かに座',
    '双子座': 'ふたご座',
    '牡羊座': 'おひつじ座',
    '水瓶座': 'みずがめ座',
    '射手座': 'いて座',
    '天秤座': 'てんびん座',
    '獅子座': 'しし座'
}

# zodiac列をひらがなに変換する関数
def convert_zodiac_to_hiragana(zodiac):
    # 座の漢字を含む部分を置換する
    for kanji, hiragana in zodiac_dict.items():
        zodiac = re.sub(kanji, hiragana, zodiac)
    return zodiac


#setting
logger = logging.getLogger()
logger.setLevel(logging.INFO)
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, QuickReply, QuickReplyButton, MessageAction, PostbackAction,
)
LINE_CHANNEL_ACCESS_TOKEN   = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
LINE_CHANNEL_SECRET         = os.environ['LINE_CHANNEL_SECRET']
LINE_BOT_API = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
LINE_HANDLER = WebhookHandler(LINE_CHANNEL_SECRET)

s3 = boto3.client('s3')

# 入力イベント内にメッセージがあるかどうかを確認
def lambda_handler(event, context):
    if 'body' in event and 'headers' in event:
        signature = event["headers"]["x-line-signature"]
        body = event["body"]
        LINE_HANDLER.handle(body, signature)
    else:
        #line_.json
        bucket = 'lineuranaibucket' # バケット名
        key = 'line_userID_target.json'
        obj = s3.get_object(Bucket=bucket, Key=key)
        text = obj['Body'].read()
        data_list = json.loads(text.decode('utf-8'))

        # データから各ユーザーの情報を取得し、プッシュメッセージを送信する
        for data in data_list:
            user_id = data["line_userID"]
            message = data["line_target"]
            
            # LINE Messaging APIに送信するデータを準備
            payload = {
                "to": user_id,
                "messages": [
                    {
                        "type": "text",
                        "text": message
                    }
                ]
            }
            
            # メッセージを送信
            try:
                response = LINE_BOT_API.push_message(user_id, TextSendMessage(text=f"今日も1日お疲れ様です\n「{message}」\nは達成できましたか？"))
                print("Push message:", message)
            except Exception as e:
                print("エラー:", e)

#line返信
@LINE_HANDLER.add(MessageEvent, message=TextMessage)
def on_message(line_event):
    profile = LINE_BOT_API.get_profile(line_event.source.user_id)
    logger.info(profile)
    user_id = profile.user_id
    print(user_id)
    #ファイルを読み込む

    #line_uranai_1.json
    bucket = 'lineuranaibucket' # バケット名
    key = 'line_uranai_1.json'
    obj = s3.get_object(Bucket=bucket, Key=key)
    text = obj['Body'].read()
    zodiac_data_1 = json.loads(text.decode('utf-8'))
    
    #line_uranai_2.json
    bucket = 'lineuranaibucket' # バケット名
    key = 'line_uranai_2.json'
    obj = s3.get_object(Bucket=bucket, Key=key)
    text = obj['Body'].read()
    zodiac_data_2 = json.loads(text.decode('utf-8'))
    
    #line_uranai_3.json
    bucket = 'lineuranaibucket' # バケット名
    key = 'line_uranai_3.json'
    obj = s3.get_object(Bucket=bucket, Key=key)
    text = obj['Body'].read()
    zodiac_data_3 = json.loads(text.decode('utf-8'))

    #line_uranai_4.json
    bucket = 'lineuranaibucket' # バケット名
    key = 'line_uranai_4.json'
    obj = s3.get_object(Bucket=bucket, Key=key)
    text = obj['Body'].read()
    zodiac_data_4 = json.loads(text.decode('utf-8'))
    
    #line_uranai_5.json
    bucket = 'lineuranaibucket' # バケット名
    key = 'line_uranai_5.json'
    obj = s3.get_object(Bucket=bucket, Key=key)
    text = obj['Body'].read()
    zodiac_data_5 = json.loads(text.decode('utf-8'))
    
    #line_uranai_6.json
    bucket = 'lineuranaibucket' # バケット名
    key = 'line_uranai_6.json'
    obj = s3.get_object(Bucket=bucket, Key=key)
    text = obj['Body'].read()
    zodiac_data_6 = json.loads(text.decode('utf-8'))



    #pandasに置き換える
    df_1 = pd.DataFrame(zodiac_data_1, columns=['zodiac', 'rank', 'link'])
    df_2 = pd.DataFrame(zodiac_data_2, columns=['zodiac', 'rank', 'link'])
    df_3 = pd.DataFrame(zodiac_data_3, columns=['zodiac', 'rank', 'link'])
    df_4 = pd.DataFrame(zodiac_data_4, columns=['zodiac', 'rank', 'link'])
    df_5 = pd.DataFrame(zodiac_data_5, columns=['zodiac', 'rank', 'link'])
    df_6 = pd.DataFrame(zodiac_data_6, columns=['zodiac', 'rank', 'link'])
    
    #漢字に変換
    df_3['zodiac'] = df_3['zodiac'].apply(convert_zodiac_to_hiragana)
    df_4['zodiac'] = df_4['zodiac'].apply(convert_zodiac_to_hiragana)
    df_5['zodiac'] = df_5['zodiac'].apply(convert_zodiac_to_hiragana)


    df = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6])
    dfs = {}
    for zodiac in df_1['zodiac']:
        df_1_temp = df_1[df_1['zodiac'] == zodiac]
        df_2_temp = df_2[df_2['zodiac'] == zodiac]
        df_3_temp = df_3[df_3['zodiac'] == zodiac]
        df_4_temp = df_4[df_4['zodiac'] == zodiac]
        df_5_temp = df_5[df_5['zodiac'] == zodiac]
        df_6_temp = df_6[df_6['zodiac'] == zodiac]

        df_combined = pd.concat([df_1_temp, df_2_temp, df_3_temp, df_4_temp, df_5_temp, df_6_temp])
        df_combined_sorted = df_combined.sort_values(by='rank')
        dfs[zodiac] = df_combined_sorted
    
    
    message = line_event.message.text.lower()
    print("Received message:", message) 
    if message in ['占い', 'うらない', '占いをする', 'うらないをする', '占う', 'うらなう']:
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='あなたの星座はどれですか？',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="おひつじ座", data="おひつじ座", text="おひつじ座")),
                        QuickReplyButton(action=PostbackAction(label="おうし座", data="おうし座", text="おうし座")),
                        QuickReplyButton(action=PostbackAction(label="ふたご座", data="ふたご座", text="ふたご座")),
                        QuickReplyButton(action=PostbackAction(label="かに座", data="かに座", text="かに座")),
                        QuickReplyButton(action=PostbackAction(label="しし座", data="しし座", text="しし座")),
                        QuickReplyButton(action=PostbackAction(label="おとめ座", data="おとめ座", text="おとめ座")),
                        QuickReplyButton(action=PostbackAction(label="てんびん座", data="てんびん座", text="てんびん座")),
                        QuickReplyButton(action=PostbackAction(label="さそり座", data="さそり座", text="さそり座")),
                        QuickReplyButton(action=PostbackAction(label="いて座", data="いて座", text="いて座")),
                        QuickReplyButton(action=PostbackAction(label="やぎ座", data="やぎ座", text="やぎ座")),
                        QuickReplyButton(action=PostbackAction(label="みずがめ座", data="みずがめ座", text="みずがめ座")),
                        QuickReplyButton(action=PostbackAction(label="うお座", data="うお座", text="うお座")),
                    ])))
                   
                   
    elif message in ['おひつじ座', 'おうし座', 'ふたご座', 'かに座', 'しし座', 'おとめ座', 'てんびん座', 'さそり座', 'いて座', 'やぎ座', 'みずがめ座', 'うお座']:
        rank_1 = dfs[message]['rank'].iloc[0]

        message1 = TextSendMessage(
            text=f"{message}の占い結果は"
        )
        message2 = TextSendMessage(
            text=f"＜{dfs[message]['rank'].iloc[0]}位＞のWebサイトは\n{dfs[message]['link'].iloc[0]}"
        )
        message3 = TextSendMessage(
            text=f"＜{dfs[message]['rank'].iloc[1]}位＞のWebサイトは\n{dfs[message]['link'].iloc[1]}"
        )
        message4 = TextSendMessage(
            text=f"＜{dfs[message]['rank'].iloc[2]}位＞のWebサイトは\n{dfs[message]['link'].iloc[2]}",
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=PostbackAction(label="他も占う", data="他も占う", text="占う")),
                QuickReplyButton(action=PostbackAction(label="今日の目標を立てる", data="今日の目標を立てる", text="今日の目標を立てる")),
                QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),

            ])

        )
            
        if rank_1 == 1:
            message5 = TextSendMessage(
                text=f"{message}のあなたは絶対いい日になりますよ！\n今日をぜひ楽しんで！！",
                quick_reply=QuickReply(items=[
                    QuickReplyButton(action=PostbackAction(label="他も占う", data="他も占う", text="占う")),
                    QuickReplyButton(action=PostbackAction(label="今日の目標を立てる", data="今日の目標を立てる", text="今日の目標を立てる")),
                    QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                ])
            )
            LINE_BOT_API.reply_message(line_event.reply_token, [message1, message2, message3, message4, message5])
            
        elif rank_1 == 2:
            message5 = TextSendMessage(
                text=f"{message}のあなたはきっといい日になりますよ！\n今日をぜひ楽しんで！",
                quick_reply=QuickReply(items=[
                    QuickReplyButton(action=PostbackAction(label="他も占う", data="他も占う", text="占う")),
                    QuickReplyButton(action=PostbackAction(label="今日の目標を立てる", data="今日の目標を立てる", text="今日の目標を立てる")),
                    QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                ])
            )
            LINE_BOT_API.reply_message(line_event.reply_token, [message1, message2, message3, message4, message5])
            
        elif rank_1 == 3:
            message5 = TextSendMessage(
                text=f"{message}のあなたはいい日になるでしょう\n今日をぜひ楽しんでください",
                quick_reply=QuickReply(items=[
                    QuickReplyButton(action=PostbackAction(label="他も占う", data="他も占う", text="占う")),
                    QuickReplyButton(action=PostbackAction(label="今日の目標を立てる", data="今日の目標を立てる", text="今日の目標を立てる")),
                    QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                ])
            )
            LINE_BOT_API.reply_message(line_event.reply_token, [message1, message2, message3, message4, message5])

        elif rank_1 == 7:
            message5 = TextSendMessage(
                text=f"きっといいことがあると思いますよ\n今日も頑張ってくださいね",
                quick_reply=QuickReply(items=[
                    QuickReplyButton(action=PostbackAction(label="他も占う", data="他も占う", text="占う")),
                    QuickReplyButton(action=PostbackAction(label="今日の目標を立てる", data="今日の目標を立てる", text="今日の目標を立てる")),
                    QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                ])
            )
            LINE_BOT_API.reply_message(line_event.reply_token, [message1, message2, message3, message4, message5])

        elif rank_1 == 8:
            message5 = TextSendMessage(
                text=f"いいことがあると願いましょう\n今日も1日頑張って！",
                quick_reply=QuickReply(items=[
                    QuickReplyButton(action=PostbackAction(label="他も占う", data="他も占う", text="占う")),
                    QuickReplyButton(action=PostbackAction(label="今日の目標を立てる", data="今日の目標を立てる", text="今日の目標を立てる")),
                    QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                ])
            )
            LINE_BOT_API.reply_message(line_event.reply_token, [message1, message2, message3, message4, message5])

        elif rank_1 == 9:
            message5 = TextSendMessage(
                text=f"ごめんなさい、、\n明日こそはいい結果をお伝えできると思います",
                quick_reply=QuickReply(items=[
                    QuickReplyButton(action=PostbackAction(label="他も占う", data="他も占う", text="占う")),
                    QuickReplyButton(action=PostbackAction(label="今日の目標を立てる", data="今日の目標を立てる", text="今日の目標を立てる")),
                    QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                ])
            )
            LINE_BOT_API.reply_message(line_event.reply_token, [message1, message2, message3, message4, message5])

        elif rank_1 == 10:
            message5 = TextSendMessage(
                text=f"今日は何事も慎重に！！\n気を付けて頑張れ！",
                quick_reply=QuickReply(items=[
                    QuickReplyButton(action=PostbackAction(label="他も占う", data="他も占う", text="占う")),
                    QuickReplyButton(action=PostbackAction(label="今日の目標を立てる", data="今日の目標を立てる", text="今日の目標を立てる")),
                    QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                ])
            )
            LINE_BOT_API.reply_message(line_event.reply_token, [message1, message2, message3, message4, message5])

        else:
            LINE_BOT_API.reply_message(line_event.reply_token, [message1, message2, message3, message4])  



    elif message == '今日の目標を立てる':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='今日の目標を立てたい場合はメニューの「今日の目標」のボタンを押して下さい\n２０時に達成できたか聞きに来ますね',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="占う", data="占う", text="占う")),
                        QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                    ])))

    elif '目標：' in message:
        # 登録するデータの準備
        register_data = {
            "line_userID": user_id,
            "line_target": message
        }
        try:
            bucket = 'lineuranaibucket'  # バケット名
            key = 'line_userID_target.json'
            
            # 既存のファイルを取得
            response = s3.get_object(Bucket=bucket, Key=key)
            existing_data = json.loads(response['Body'].read().decode('utf-8'))
            df_userID_target = pd.DataFrame(existing_data, columns=['line_userID', 'line_target'])
            df_userID_target_temp = pd.DataFrame([register_data])  # データをリストの形式で渡す
            df_userID_target = pd.concat([df_userID_target, df_userID_target_temp], ignore_index=True)  # データフレームを結合
            dict_userID_target = df_userID_target.to_dict(orient='records')  # 辞書に変換
            new_contents = json.dumps(dict_userID_target)
            s3.put_object(Body=new_contents, Bucket=bucket, Key=key)
            response_text = f'では\n「{message}」\nが達成できるように今日も頑張ってくださいね！'
        except Exception as e:
            response_text = 'ごめんなさい。\nエラー: {}'.format(str(e))
        
        # ユーザーに応答を返す
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text=response_text,
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="占う", data="占う", text="占う")),
                        QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                    ])))


    #ギャグ集
    elif message == 'ぎょうざ':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='ははは、面白いですね、、',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="占う", data="占う", text="占う")),
                        QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                    ])))
    elif message == 'ぴざ':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='私は照り焼きピザが好きです',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="占う", data="占う", text="占う")),
                        QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                    ])))
    elif message == 'きざ':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='あなたのことですか？？',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="占う", data="占う", text="占う")),
                        QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                    ])))
    elif message == 'ぎょくざ':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='座ってみたいものですねー',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="占う", data="占う", text="占う")),
                        QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                    ])))
        
        #ことわざ
    elif message == 'ことわざ':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='私は　井の中の蛙　が好きです\nこのことわざ続きがあるの知っていますか？',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="知ってる！", data="知ってる！", text="知ってる！")),
                        QuickReplyButton(action=PostbackAction(label="知らない", data="知らない", text="知らない")),
                    ])))
    elif message == '知ってる！':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='是非打ってみてください\n全部ひらがなでお願いしますね',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="そんなのいいから占う", data="そんなのいいから占う", text="占う")),
                        QuickReplyButton(action=PostbackAction(label="やっぱり知らない", data="やっぱり知らない", text="知らない")),
                    ])))
    elif message == '知らない':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='答えをお教えしましょうか？',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="教えて！", data="教えて！", text="教えて！")),
                        QuickReplyButton(action=PostbackAction(label="別にいいや", data="別にいいや", text="別にいいや")),
                    ])))
    elif message == '教えて！':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='井の中の蛙大海を知らずされど空の深さ(青さ)を知る　です\nもともとネガティブな意味が\n「狭い世界で一つのことを突き詰めたからこそ、その世界の深いところまで知ることができた」\nという素敵な意味に変わる面白いことわざです',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="占う", data="占う", text="占う")),
                        QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                    ])))
    elif message == '別にいいや':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='そうですか、、',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="占う", data="占う", text="占う")),
                        QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                    ])))
    elif message == 'たいかいをしらず':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='実はまだ続きがあるんですねー\n是非よければ全文ひらがな打ってみてください',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="占う", data="占う", text="占う")),
                        QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                        QuickReplyButton(action=PostbackAction(label="それは知らない", data="それは知らない", text="知らない")),
                    ])))
    elif message in['たいかいをしらずされどそらのあおさをしる','たいかいをしらずされどそらのふかさをしる']:
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='おお！！詳しいですね！\nとても博識な方なんですね！\nそんなあなたの運勢はきっといいはずですよ',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="占う", data="占う", text="占う")),
                        QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                    ])))
        

    elif message == 'せいざ':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='正座するのは苦手です、、\nちなみに私の星座はかに座です\n是非私の運勢も占ってみてください',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="占う", data="占う", text="占う")),
                        QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                    ])))
    elif message == 'どげざ':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='何か悪いことでもしたんですか？',
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=PostbackAction(label="占う", data="占う", text="占う")),
                        QuickReplyButton(action=PostbackAction(label="ばいばい", data="ばいばい", text="ばいばい")),
                    ])))
      
    elif message == 'ばいばい':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='また来てくれると嬉しいです'))
            
    elif message == '出来た！':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='流石です！\n明日もその調子で頑張りましょう！'))
            
    elif message == 'まあまあかな':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='よく頑張りました\n明日はきっと今日より上手くいきますよ'))
            
    elif message == 'あんまりかも':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='そんな日もありますよね\nもう今日はゆっくり休んでくださいね'))
            
    elif message == 'ダメダメだー':
        LINE_BOT_API.reply_message(line_event.reply_token,
            TextSendMessage(text='あらら\n明日こそは達成できますよ！\n明日も待ってますね'))

    elif message == 'ソックス':
        LINE_BOT_API.reply_message(line_event.reply_token, StickerSendMessage(package_id='8515',sticker_id='16581254'))

    else:
        LINE_BOT_API.reply_message(line_event.reply_token, StickerSendMessage(package_id='11537',sticker_id='52002744'))
        return

