from django.contrib import admin

from form_app4.models import Message

# Register your models here.
admin.site.register(Message)

# Na koniec mówimy o modyfikowaniu tego co widzimy w formularzu.
# A co gdybyśmy chcieli, żeby widok znajdujący się w panelu administratora
# wyglądał inaczej. Możemy go dowolnie zmieniać.
# Popatrzmy jak teraz wyświetla się lista. (mamy reprezentacje napisową)
# A co gdybyśmy chcieli, żeby wyświetlały się tylko wybrane pola.
#
@admin.register(Message)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "body")

# Podkreślamy, że w modelach mamy models.Model, a w adminie admin.ModelAdmin