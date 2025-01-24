from typing import Any, Text, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import pandas as pd

class ActionAskTicket(Action):
    def name(self) -> Text:
        return "action_ask_ticket"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        senderid = tracker.sender_id.split("/")[-1]
        registered_user = pd.read_csv("registered_number.csv")

        if int(senderid) in list(registered_user["client_user"]):
            message = {
                "interactive": {
                    "type": "list",
                    "body": {
                        "text": "Apakah Sobat ingin bertanya terkait status update tiket dari menu berikut:"
                    },
                    "action": {
                        "button": "Menu",
                        "sections": [
                            {
                                "title": "Pilihan:",
                                "rows": [
                                    {
                                        "id" :"MOB0000002420001",
                                        "title": "MOB0000002420001",
                                        "description": "Tiket MOB0000002420001",
                                    },
                                    {
                                        "id" :"MOB0000002420002",
                                        "title": "MOB0000002420002",
                                        "description": "Tiket MOB0000002420002",
                                    },
                                    {
                                        "id" :"MOB0000002420003",
                                        "title": "MOB0000002420003",
                                        "description": "Tiket MOB0000002420003",
                                    },
                                    {
                                        "id" :"MOB0000002420004",
                                        "title": "MOB0000002420004",
                                        "description": "Tiket MOB0000002420004",
                                    },
                                    {
                                        "id" :"MOB0000002420005",
                                        "title": "MOB0000002420005",
                                        "description": "Tiket MOB0000002420005",
                                    }
                                ],
                            },
                        ],
                    }
                    # end action
                }
                # end interactive
            }
            dispatcher.utter_message(attachment = message)
            return []
        else:
            dispatcher.utter_message \
                (text = "Mohon maaf, nomor Sobat belum terdaftar dalam layanan ini.\n\nSilakan hubungi teman SIERA di Service Desk 1500234 atau klik https://myssc.pertamina.com untuk dapat menikmati layanan kami.")
            return [FollowupAction(name='action_restart')]
