from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions # For IsAuthenticated, etc.
from rest_framework_simplejwt.authentication import JWTAuthentication # Assuming JWT for authentication

from django.shortcuts import get_object_or_404 # Helper for retrieving objects or raising 404
from ..models.warehouse import GeneralCargo, CargoItemRelease, OperationTable, Contract
from ..serializers.warehouse_serializers import GeneralCargoSerializer, CargoItemReleaseSerializer, OperationTableSerializer, ContractSerializer

# --- General Cargo Views ---
class GeneralCargoListCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        List all general cargo entries.
        """
        general_cargo_items = GeneralCargo.objects.all()
        serializer = GeneralCargoSerializer(general_cargo_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        Create a new general cargo entry.
        """
        serializer = GeneralCargoSerializer(data=request.data)
        if serializer.is_valid():
            # Optional: Link company_user or company to the authenticated user
            # Example: if request.user has a related CompanyUser instance
            # try:
            #     company_user_instance = request.user.companyuser
            #     serializer.save(company_user=company_user_instance)
            # except AttributeError:
            #     # Handle case where user might not have an associated CompanyUser
            #     # Or if you don't want to auto-assign it always
            #     serializer.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GeneralCargoDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        """
        Helper method to get a GeneralCargo object or raise 404.
        """
        return get_object_or_404(GeneralCargo, pk=pk)

    def get(self, request, pk, format=None):
        """
        Retrieve a single general cargo entry.
        """
        general_cargo = self.get_object(pk)
        serializer = GeneralCargoSerializer(general_cargo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """
        Update an existing general cargo entry (full update).
        """
        general_cargo = self.get_object(pk)
        serializer = GeneralCargoSerializer(general_cargo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        """
        Partially update an existing general cargo entry.
        """
        general_cargo = self.get_object(pk)
        serializer = GeneralCargoSerializer(general_cargo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete a general cargo entry.
        """
        general_cargo = self.get_object(pk)
        general_cargo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Cargo Item Release Views ---
class CargoItemReleaseListCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        cargo_items = CargoItemRelease.objects.all()
        serializer = CargoItemReleaseSerializer(cargo_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CargoItemReleaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CargoItemReleaseDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(CargoItemRelease, pk=pk)

    def get(self, request, pk, format=None):
        cargo_item = self.get_object(pk)
        serializer = CargoItemReleaseSerializer(cargo_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        cargo_item = self.get_object(pk)
        serializer = CargoItemReleaseSerializer(cargo_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        cargo_item = self.get_object(pk)
        serializer = CargoItemReleaseSerializer(cargo_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cargo_item = self.get_object(pk)
        cargo_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --- Operation Table Views ---
class OperationTableListCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        operations = OperationTable.objects.all()
        serializer = OperationTableSerializer(operations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = OperationTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OperationTableDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(OperationTable, pk=pk)

    def get(self, request, pk, format=None):
        operation = self.get_object(pk)
        serializer = OperationTableSerializer(operation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        operation = self.get_object(pk)
        serializer = OperationTableSerializer(operation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        operation = self.get_object(pk)
        serializer = OperationTableSerializer(operation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        operation = self.get_object(pk)
        operation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --- Contract Views ---
class ContractListCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        contracts = Contract.objects.all()
        serializer = ContractSerializer(contracts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ContractSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContractDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Contract, pk=pk)

    def get(self, request, pk, format=None):
        contract = self.get_object(pk)
        serializer = ContractSerializer(contract)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        contract = self.get_object(pk)
        serializer = ContractSerializer(contract, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        contract = self.get_object(pk)
        serializer = ContractSerializer(contract, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contract = self.get_object(pk)
        contract.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)