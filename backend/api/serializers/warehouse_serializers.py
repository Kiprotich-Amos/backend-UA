from rest_framework import serializers
from ..models.warehouse import GeneralCargo, CargoItemRelease, OperationTable, Contract


class GeneralCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralCargo
        fields = ["consignment_no", "kra_no", "company", "company_user", "transporter", "no_bags", "units_measure", "net_weight", "gross_weight", "status_one"]
        read_only_fields = ["created_at"]

class CargoItemReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoItemRelease
        fields = ["id", "general_cargo", "company_user", "transporter", "no_bags", "net_weight", "gross_weight", "status", "created_at"]
        read_only_fields = ["created_at"] 

class OperationTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationTable
        fields = ["id", "company_user", "name_operation", "company", "price_set"]

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "contract_name", "contract_client", "contract_duration", "expected_cargo", "contract_unit_price", "contract_start"]