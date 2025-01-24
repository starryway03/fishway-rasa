import json

data = {'sender': 'coster/whatsapp-cloud/342066988999062/jamobai/689b83aa561d11ef93136fefc8d9c8f7/6287789805088', 'message': '<nfm_relpy> "{\\"screen_0_TextInput_0\\":\\"Thor\\",\\"screen_0_RadioButtonsGroup_1\\":\\"1_Belum_Bersedia\\",\\"screen_0_DatePicker_2\\":\\"2024-12-19\\",\\"screen_0_OptIn_3\\":true,\\"flow_token\\":\\"RECOMMEND\\"}"', 'metadata': {'timestamp': '1734571476', 'message_id': 'wamid.HBgNNjI4Nzc4OTgwNTA4OBUCABIYIDI5Rjk5QzU1RDY2QkI4NUMxRDU3MEM4RjE1MkIzQTc2AA==', 'sender_name': 'Thoriqul Fahri', 'bot_display_id': '6285135595046'}}
print(data)
msg = data.get('message')
print(msg)
json_obj = json.loads(msg.split("<nfm_relpy>")[1])
print(json_obj)