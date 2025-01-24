from typing import Any, Text, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import pandas as pd

class ActionAgent(Action):
    def name(self) -> Text:
        return "action_agent"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        senderid = tracker.sender_id.split("/")[-1]
        registered_user = pd.read_csv("registered_number.csv")

        if int(senderid) in list(registered_user["client_user"]):
            agent = {
                "type": "is_helpdesk",
                "division_id": "53974624c01a11eca0b8a95aa68aa97c",
                "message": "Mohon tunggu sebentar, Sobat akan segera terhubung dengan Agen kami..."
            }
            dispatcher.utter_message(attachment=agent)
            return []
        else:
            dispatcher.utter_message(
                text="Mohon maaf, nomor Sobat belum terdaftar dalam layanan ini.\n\nSilakan hubungi teman SIERA di Service Desk 1500234 atau klik https://myssc.pertamina.com untuk dapat menikmati layanan kami.")
            return [FollowupAction(name='action_restart')]

