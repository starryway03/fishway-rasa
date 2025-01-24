from typing import Any, Text, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionTower(Action):
    def name(self) -> Text:
        return "action_tower"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = {
            "interactive": {
                "type": "list",
                "body": {
                    "text": "Silahkan Sobat pilih Tower dari menu berikut ini:"
                },
                "action": {
                    "button": "Menu",
                    "sections": [
                        {
                            "title": "Pilihan:",
                            "rows": [
                                {
                                    "id": "ICT",
                                    "title": "ICT",  # 3 chara
                                    "description": "Tower ICT",  # 9 chara
                                },
                                {
                                    "id": "Finance",
                                    "title": "Finance",  # 7 chara
                                    "description": "Tower Finance",  # 13 chara
                                },
                                {
                                    "id": "HC",
                                    "title": "HC",  # 2 chara
                                    "description": "Tower HC",  # 8 chara
                                },
                                {
                                    "id": "Procurement",
                                    "title": "Procurement",  # 11 chara
                                    "description": "Tower Procurement",  # 17 chara
                                }
                            ],
                        },
                    ],
                }
                # end action
            }
            # end interactive
        }
        dispatcher.utter_message(text="Silahkan pilih Tower yang Sobat cari terlebih dahulu.")
        dispatcher.utter_message(attachment=message)
        return []
