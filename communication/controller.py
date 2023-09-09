from django.db import transaction
from communication.models import FlowDefinition, FlowExecution, FlowElement, MessageElement
from communication.models import FlowTriggerType, FlowElementType
from lead.models import Lead
from registration.models import Account
import json


class Controller:
    def communication_event(self, event):
        event_type = event.get('event')
        if event_type == FlowTriggerType.NOVO_LEAD.value:
            flow_execution, elements = self.__create_new_lead_flow(event.get('record'))
        self.__start_execution(elements=elements, flow_execution=flow_execution)

    def __start_execution(self, elements, flow_execution):
        print(elements)
        pass

    @transaction.atomic
    def __create_new_lead_flow(self, lead_data):
        owner_id = lead_data.get('owner')
        flow_definition = self.__get_new_lead_flow_definition(owner_id=owner_id)
        if not flow_definition:
            return
        lead = Lead.objects.get(id=lead_data.get('id'))
        owner = Account.objects.get(id=owner_id)
        definition = json.loads(flow_definition.definition)
        elements_data = self.__get_element(definition=definition)
        flow_execution = FlowExecution.objects.create(flow_definition=flow_definition, lead=lead, owner=owner)
        created_elements = self.__create_elements(elements_data=elements_data, flow_execution=flow_execution, lead_data=lead_data)
        return flow_execution, created_elements

    def __get_element(self, definition):
        elements_data = dict()
        elements = definition.get('definition').get('elements')
        for element in elements:
            if element.get('type') == FlowElementType.MENSAGEM.value:
                elements_data[FlowElementType.MENSAGEM.value] = {
                    'value': element.get('params').get('value')
                }
        return elements_data

    def __create_elements(self, elements_data, flow_execution, lead_data):
        elements = []
        index = 0
        for key, value in elements_data.items():
            if key == FlowElementType.MENSAGEM.value:
                raw_value = value.get('value')
                value = raw_value.replace('${first_name}', lead_data.get('first_name'))
                flow_element = FlowElement.objects.create(flow_execution=flow_execution, name=FlowElementType.MENSAGEM.value, index=index)
                message_element = MessageElement.objects.create(flow_element=flow_element, content=value)
                elements.append((flow_element, message_element))
            index = index + 1
        return elements

    def __get_new_lead_flow_definition(self, owner_id):
        return FlowDefinition.objects.filter(owner=owner_id, trigger=FlowTriggerType.NOVO_LEAD.value, is_active=True).first()
