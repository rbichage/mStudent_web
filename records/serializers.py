from rest_framework import serializers

from records.models import Student, PrimaryExam


class StudentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Student
            field = "__all__"

class PrimaryExamSerializer(serializers.ModelSerializer):
        class Meta:
            model = PrimaryExam
            field = "__all__"
