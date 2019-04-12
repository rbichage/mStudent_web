from django.contrib.auth.models import User
from rest_framework import serializers

from records.models import Student, PrimaryExam, SecondaryExam, UniversityExam, Certificate, Payment


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class PrimaryExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryExam
        fields = "__all__"


class SecondaryExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryExam
        fields = "__all__"


class UniversityExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityExam
        fields = "__all__"


class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'id',
        )


class PaymentSerialier(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
