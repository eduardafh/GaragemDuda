from rest_framework.serializers import ModelSerializer

from core.models import Veiculo, veiculo


class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"