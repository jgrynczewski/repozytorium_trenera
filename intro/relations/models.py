from django.db import models

# Mamy:
# - OneToOne Field
# - OneToMany Field (Foreign Key)
# - ManyToMany Field

#####################
##### OneToMany #####
#####################

# Parent-child relationship aka One-to-many (or Many-to-one, depending on who we are taking about) relationship
# Single language can have multiple frameworks, but a framework is written in just one language
# Ex. Python and Django
# Django is written in Python, but also Flask is written in Python (many-to-one)
# Python has Django, Flask, Bottle and many different frameworks available (one-to-many)
# class Language(models.Model):
#    ...
#
# class Framework(models.Model):
#    ...

class Language(models.Model):
    name = models.CharField(max_length=10)

    # To na późniejszym etapie
    def __str__(self):
        return f"{self.name}"

# class Framework(models.Model):
#     name = models.CharField(max_length=10)

# Now, foreign key field. We can put the foreign key on either table but it makes more sense conceptually
# to put it on the child, because the child only has the one parent (so it is al little bit more easy to
# thing about it in that way).
class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE) #this means that this column (field) will reference another table

    # To na późniejszym etapie
    def __str__(self):
        return f"{self.name}"
# makemigrations
# migrate
# Oglądamy tabele w db browser (zwracamy uwagę na nazwę kolumny language_id, mimo że my nazwaliśmy ją
# language).

# shell

# (C) w crud
# >>> from relations.models import Language, Framework

# >>> python = Language(name="python")
# >>> python.save()
# >>> django = Framework(name="django")
# >>> django.save()
#   File "C:\Users\Ania\PycharmProjects\test_venv\venv\lib\site-packages\django\db\backends\sqlite3\base.py", line 396, in execute
#     return Database.Cursor.execute(self, query, params)
# django.db.utils.IntegrityError: NOT NULL constraint failed: relations_framework.language_id

# >>> django = Framework(name="django", language="python")
# ValueError: Cannot assign "'python'": "Framework.language" must be a "Language" instance.

# >>> python
# <Language: Language object (1)>

# >>> django = Framework(name="django", language=python)
# >>> django.save()
# >>> flask = Framework.objects.create(nam="fask", language=python)

# >>> bottle = Framework()
# >>> bottle.name = "bottle"
# >>> bottle.language = python
# >>> bottle.save()

# Patrzymy w db browser
# Mówimy o 1 w kolumnie language_id - oznacza id w tabeli language

# Wracamy do shella i dodajemy jeszcze inny język
# >>> Language.objects.create(name="java")
# <Language: Language object (2)>

# >>> Framework.objects.create(name="spring", language=...)
# no ale teraz nie mamy obiektu klasy language.
# >>> java = Language.objects.get(pk=2)
# >>> java
# <Language: Language object (2)>
# >>> Framework.objects.create(name="spring", language=java)
# <Framework: Framework object (4)>

# Oglądamy jeszcze raz w db browser

# Teraz zapytania (R) w crud

# Give me all frameworks
# >>> Framework.objects.all()
# <QuerySet [<Framework: Framework object (1)>, <Framework: Framework object (2)>, <Framework: Framework object (3)>], <Framework: Framework object (4)>]>

# Dorabiamy __str__ dla obu modeli

# >>> Framework.objects.all()
# <QuerySet [<Framework: django>, <Framework: bottle>, <Framework: flask>, <Framework: spring>]>
# OK

# >>> Wszystkie zawierające a w nazwie.
# >>> Framework.objects.filter(name__contains="a")
# <QuerySet [<Framework: django>, <Framework: flask>]>

# No ale tym razem mamy relacje. Jak użyć relacji w zapytaniu ?

# Give me all frameworks for python language

# Możemy klasycznie (czyli pobieramy obiekt i po nim wyszukujemy)
# >>> python = Language.objects.get(name="python")
# >>> python
# <Language: python>
# >>> Framework.objects.filter(language=python)
# <QuerySet [<Framework: django>, <Framework: bottle>, <Framework: flask>]>

# No ale w bazie mamy kolumnę language_id, może po niej można?
# >>> python.id
# 1
# >>> Framework.objects.filter(language_id=1)
# <QuerySet [<Framework: django>, <Framework: bottle>, <Framework: flask>]>

# A można jeszcze inaczej. Wykorzystując operator, który już poznaliśmy (lookup operator)
# >>> Framework.objects.filter(language__id=1)
# <QuerySet [<Framework: django>, <Framework: bottle>, <Framework: flask>]>
# >>> Framework.objects.filter(language__name="python")
# <QuerySet [<Framework: django>, <Framework: bottle>, <Framework: flask>]>

# A odkąd language_id to ta sama kolumna co language możemy równie dobrze napisać:
# >>> Framework.objects.filter(language_id__name="python")
# <QuerySet [<Framework: django>, <Framework: bottle>, <Framework: flask>]>

# No i dalej możemy używać lookup operator na polu tabeli powiązanej.
# >>> Framework.objects.filter(language_id__name__startswith="py")
# <QuerySet [<Framework: django>, <Framework: bottle>, <Framework: flask>]>

# >>> Framework.objects.filter(language_id__name__startswith="pa")
# <QuerySet []>

# A jak odpytywać w drugą stronę, czyli od rodzica.
# Wszystkie języki, które posiadają framework o nazwie Spring.
# Language.objects.filter(framework__name="spring")
# <QuerySet [<Language: java>]>
# framework wzięło się od nazwy klasy (pierwsz litera z małej)

####################
##### OneToOne #####
####################

# Bardzo podobny typ pola (OneToOne Field będzie się zachowywał w ten sam sposób,
# z tą różnicą, że zapytanie odwrotne zwróci obiekt klasy Language, a nie queryset.
# OneToOne Field to Foreign Key z unique=True z dokładnością do zwracanej klasy
# OneToOne -> instancję, ForeignKey -> QuerySet.

######################
##### ManyToMany #####
######################

# This is not like parent-child relation.
# One table has multiple instances of other table and reverse.
# Ex. movies and characters in those movies
# Przykład:
# postać- Kapitan Ameryka, występuje w filmach: Avengers, Captian America, i Thor
# ale możemy też w drugą stronę
# film- Avengers, występują w nim: Captain America, Iron Man, Thor, Hulk

# Nie jest to relacja typu rodzic dziecko, gdzie dziecko może mieć tylko jednego rodzica.

class Movie(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"


# class Character(models.Model):
#     name = models.CharField(max_length=10)
#
#     def __str__(self):
#         return f"{self.name}"

# No i teraz musimy je ze sobą powiązać. Typ relacji: ManyToMany field
# Możemy umieścić to pole w dowolnej z tabeli, ale koncepcyjnie lepiej umieścić
# ją w tabeli, która jest niejako na niższym poziomie (niskopoziomowa).
# Tutaj film możemy potraktować intuicyjnie jako wyżejpoziomowy (gromadzi postacie).
# Relacja jest symetryczna, więc moglibyśmy równie w innym kontekście uznać, że postać
# jest na wyższym poziomie.
# Film jest wyżej, więc relację ustawiamy na postaci (niżej)

class Character(models.Model):
    name = models.CharField(max_length=10)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return f"{self.name}"

# makemigrations, migrate
# patrzymy na db browser
# Widzimy tabelę movie i character.
# Ale nie ma trzeciej kolumny (jak to było w tabeli framework - kolumna language_id)
# Nie ma, bo orm relacje many-to-many zgodnie z zasadami normalizacji (dekompozycji bazy danych)
# implementuje za pomocą dodatkowej tabeli - relations_character_movies <aplikacja_tabela_kolumna>.

# Jeżeli zostanie trochę czasu, powiemy dlaczego Django tak to robi. Wynika to z tzw. procesu
# normalizacji. Jest to zagadnienie z projektowania baz danych. Czy ktoś spotkał się już z tym
# terminem ?

# shell
# >>> avengers = Movie(name='Avengers')
# >>> avengers.save()
# >>> captain_america = Character(name='Captain America')
# >>> captain_america.save()

# Patrzymy w db browser i widzimy wpis w Character i w Movie.
# Ale w relations_character_movies nie ma żadnego wpisu.
# I tu widzimy różnicę pomiędzy polem Foreign key, a polami
# ManyToMany czy OneToMany. Foreign key musi istnieć, podczas gdy
# OneToMany, czy ManyToMany już nie.

# Żeby stworzyć taką relację musimy użyć jeszcze innej (nowej składni).
# >>> captain_america.movies.add(avengers)

# I widzimy wpis w relations_character_movies. Widzimy, że kapita ameryka występuje
# w Avengers (ew. Avengersi mają w obsadzie kapitana amerykę).
# Tak czy inaczej w tabelce widzimy jak są ze sobą dane powiązane.

# Możemy na skróty.
# >>> captain_america.movies.create(name="Civil War)
# <Movie: Civil War>

# Zwróciło instancję klasy Movie.
# Patrzymy w bazie. Nowy wpis w dwóch tabelkach: relations_movie i relations_character_movies

# Pozostaje kwestia tego jak odpytywać po takiej relacji. Bardzo podobnie jak to było
# w relacji klucza głównego.

# Wszystko co było pozostaje aktualne. Plus
# >>> Character.objects.filter(movies__name="Civil War")
# <QuerySet [<Character: Captain America>]>

# W drugim kierunku
# >>> Movie.objects.filter(character__name="Captain America")
# <QuerySet [<Movie: Avengers>, <Movie: Civil War>]>
# Tutaj nie mieliśmy kolumny character. character wzieło się z nazwy klasy.

# Możemy też w innym sposób wykonać to zapytanie, poprzez odwołanie się bezpośrednio do "wartości w kolumnie"
# >>> captain = Character.objects.get(name="Captain America")
# >>> captain.movies.all()
# <QuerySet [<Movie: Avengers>, <Movie: civil war>]>
# W drugą stronę (tu nietypowo, kolumny nie ma - character z nazwy klasy ale tym razem z dodatkiem _set)
# >>> avengers = Movie.objects.get(name='Avengers')
# >>> avengers.character_set.all()
# <QuerySet [<Character: Captain America>]>

                        ####################
                        ### NORMALIZACJA ###
                        ####################


# Przy tworzeniu bazy danych może okazać się, że chcemy trzymać w bazie:
# dane o firmie, dane o pracownikach, dane o klientach, o produktach, o transakcjach,
# o oteczeniu biznesowym, ... Pojawia się pytanie jak tą bazę zaprojektować.
# Pierwszy strzał: trzymamy wszystko w jednej ogromnej tabeli.
# Dużo minusów, a największy masa powtórzeń, złożoność pamięciowa eksponencjalna ....
# Wobec tego rozbijamy tą jedną wielką tabelę na mniejsze.
# Ale jak bardzo mam ją rozbijać (normalizować). Skoro mam podzielić dużą tabelę na mniejsze,
# to jak długo mam dzielić, do jak małych tabel. Z pomocą przychodzą zasady noramlizacji
# zebrane w tzw. postaciach normalnych - zbiór wymagań jakie musi spełniać tabela, żeby znaleźć się
# w określonej postaci.

# W architekturze (projektowaniu) bazy danych wyróżniamy kilka postaci:
# - Pierwsz postać normalna (1NF), Druga (2NF), Trzecia (3NF), Boyce'a-codde (BCNF lub 3.5NF) i czwarta (4NF),
# piąta (5NF).

# Trzecia postać normalna jest traktowana jako postać właściwa. Możemy powiedzieć, że celem
# normalizacji jest doprowadzenie tabeli do trzecie postaci normalnej.
# Żeby tabela character była w 3NF relację wiele do wielu należy zaimplementować jako odrębną tabelę.

# Np. 1NF oznacza: tabela posiada klucz główny + wartości w kolumnach są atomowe (przykład: kolumna
# adres mogłaby mieć wartość: ul. Armii Krajowej 75 05-075 Warszawa, ale to nie jest wartość atomowa,
# żeby tabela miała 1NF należy tą wartość rozbić na kilka kolumn: ulica, numer, kod pocztowy, miasto.
# 2NF to 1NF + dodatkowe wymagania (żadna niekluczowa kolumna nie może zależeć od innej niekluczowej kolumny),
# niekluczowa kolumna = kolumna nie z kluczem głównym, innymi słowy wszystkie kolumny zależą wyłącznie od
# klucza głównego.

# Przykład niekluczowa kolumna zaludnienie_miasta zależy od niekluczowej kolumny miasto (bo jest to
# charakterystyka miasta, a nie osoby - a wpisy w naszej tabeli to osoby).

# ============================================                                 ===============================
#  id | imie | miasto   | zaludnienie miasta |                                  id  |   miasto | zaludnienie |
# ============================================                                 ===============================
#  1 | Adam  | Warszawa |       1.7 mln      |              = >                  1 | Warszawa |  1.7 mln    |
#  2 | Jan   | Kraków   |       0.7 mln      |   Żeby spełnić 2 NF przenosimy    2 | Kraków   |  0.7 mln    |
#  3 | Ewa   | Warszawa |       1.7 mln      |   zależność do oddzielnej tabeli  ============================
# ============================================

# A w naszej tabeli wprowadzamy klucz obcy (relację) do nowej tabeli

# =========================
#   id | imię | miasto_id |
# =========================
#   1  | Adam |     1     |
#   2  | Jan  |     2     |
#   3  | Ewa  |     1     |
#   =======================

# Powtórzenie wciąż wystąpują (miasto_id) ale zminimalizowaliśmy rozmiar powtarzanych wartości.

# 3NF - 2NF + wszystkie niekluczowe kolumny muszą zależeć od pełnego klucza.
# Wymagania dla prostego (jednokolumnowego) klucza głównego redukuje się do wymagania na 2NF.
# Sytuacja się lekko komplikuje jeżeli mamy w naszej tabeli złożony klucz główny (wielokolumnowy).

