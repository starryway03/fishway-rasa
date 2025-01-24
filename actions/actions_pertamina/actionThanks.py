from typing import Any, Text, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionThanks(Action):
    def name(self) -> Text:
        return "action_thanks"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = {
            "interactive": {
                "type": "list",
                "body": {
                    "text": "Berikan penilaian Sobat dari skala 1 sampai 5 dengan memilih dari menu berikut:"
                },
                "action": {
                    "button": "Menu",
                    "sections": [
                        {
                            "title": "Pilihan:",
                            "rows": [
                                {
                                    "id": "Bintang1",
                                    "title": "Bintang 1",
                                    "description": "Sangat Kurang Baik",
                                },
                                {
                                    "id": "Bintang2",
                                    "title": "Bintang 2",
                                    "description": "Kurang Baik",
                                },
                                {
                                    "id": "Bintang3",
                                    "title": "Bintang 3",
                                    "description": "Lumayan",
                                },
                                {
                                    "id": "Bintang4",
                                    "title": "Bintang 4",
                                    "description": "Baik",
                                },
                                {
                                    "id": "Bintang5",
                                    "title": "Bintang 5",
                                    "description": "Sangat Baik",
                                }
                            ],
                        },
                    ],
                }
                # end action
            }
            # end interactive
        }
        dispatcher.utter_message(
            text="Terima kasih ya Sobat, SIERA senang bisa membantu kamu.\n\nBantu SIERA lebih baik lagi ya dalam melayani Sobat dengan memberikan positive feedback agar SIERA terus bertumbuh dan memberikan layanan terbaik bagi Sobat SIERA.")
        dispatcher.utter_message(attachment=message)
        return []
