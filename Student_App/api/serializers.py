from Student_App.models import Student
from rest_framework     import serializers


class CountStudentSerializer(serializers.Serializer):
    total_no_of_students = serializers.IntegerField()

class StatusStudentSerializer(serializers.Serializer):
    active_students      = serializers.IntegerField()
    inactive_students    = serializers.IntegerField()


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  Student
        fields =  ('name','age','college_year','roll_number','active')                                                                

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is Too Short")
        return value

    def validate(self, data):
        if len(data['roll_number']) != 10:
            raise serializers.ValidationError("Roll number should be 10 digits")
        if data['age'] < 16:
            raise serializers.ValidationError("Age should be greater than 16")
        return data        	





