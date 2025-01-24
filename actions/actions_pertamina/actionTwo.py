from typing import Any, Text, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionAccount(Action):
    def name(self) -> Text:
        return "action_account"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = {
            "interactive": {
                "type": "list",
                "body": {
                    "text": "Silahkan Sobat pilih informasi tentang Account and Access dari menu berikut ini:"
                },
                "action": {
                    "button": "Menu",
                    "sections": [
                        {
                            "title": "Pilihan:",
                            "rows": [
                                {
                                    "id": "DigitalSignature",
                                    "title": "Digital Signature",  # 17 chara
                                    "description": "Info tentang Digital Signature",  # 30 chara
                                },
                                {
                                    "id": "VPN",
                                    "title": "VPN",  # 3 chara
                                    "description": "Info tentang VPN",  # 16 chara
                                },
                                {
                                    "id": "Wifi",
                                    "title": "Wi-Fi",  # 5 chara
                                    "description": "Info tentang Wi-Fi",  # 18 chara
                                }
                            ],
                        },
                    ],
                }
                # end action
            }
            # end interactive
        }
        dispatcher.utter_message(text="Berikut informasi tentang Account and Access yang bisa Sobat pilih.")
        dispatcher.utter_message(attachment=message)
        return []
