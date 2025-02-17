from rest_framework import serializers
from lab.models import Lab, Pic, Label

class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pic
        fields = ['url', 'fromS3']

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['shortname', 'fullname']

class LabSerializer(serializers.ModelSerializer):
    isSaved = serializers.SerializerMethodField()
    pic = PicSerializer(many=True, read_only=True)
    label = LabelSerializer(many=True, read_only=True)
    class Meta:
        model = Lab
        fields = ['id', 'name', 'link', 'intro', 'people', 'funding', 'dep', 'approved', 'isSaved', 'emails','pic', 'label']

    def get_isSaved(self, obj):
        user_id = self.context['request'].user.id
        print(self.context['request'])
        print("user_id: ", user_id)
        if not user_id:
            return False
        saved_labs = self.context.get('saved_labs', set())
        return int(obj.id) in saved_labs


class CreateLabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = ['name', 'link', 'intro', 'people', 'funding', 'dep', 'emails', 'creator_id']

class SimpleLabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = ['id', 'name', 'link', 'dep']


class LabSerializerLabPage(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields= ['id', 'name', 'link', 'people', 'intro', 'emails', 'dep']
