from rest_framework import serializers
from api import models

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ["author_name"]


class BookSerializer(serializers.ModelSerializer):
    author_name = AuthorSerializer(many=True)

    class Meta:
        model = models.Book
        fields = "__all__"

    def create(self, validated_data):
        author_name = validated_data.pop('author_name')
        book = models.Book.objects.create(**validated_data)
        for author in author_name:
            author, created = models.Author.objects.get_or_create(author_name=author['author_name'])
            book.author_name.add(author)
        book.save()
        return book
    

    def update(self, instance, validated_data):
        authors_list = []
        try:
            author_name = validated_data.pop('author_name')
            for author in author_name:
                print(author)
                author, created = models.Author.objects.get_or_create(author_name=author['author_name'])
                authors_list.append(author)
        except:
            authors_list = []
            for i in instance.author_name.all():
                authors_list.append(i)

        instance.author_name.set(authors_list)
        instance.title = validated_data.get('title', instance.title)
        instance.publication_date=validated_data.get('publication_date', instance.publication_date)
        instance.save()
        return instance