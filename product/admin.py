from django.contrib import admin

# Register your models here.
from .models import ChatMessages, Product , Category , Brand , ProductImages, ProductChat

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductImages)
admin.site.register(ProductChat)

class ChatMessagesAdmin(admin.ModelAdmin):
     list_display = ('id', 'chat', 'other_user', 'message_user', 'message', 'created')

admin.site.register(ChatMessages, ChatMessagesAdmin)
