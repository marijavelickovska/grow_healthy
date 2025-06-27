from django.db import migrations


def create_meal_types(apps, schema_editor):
    Meal = apps.get_model('recipe', 'Meal')
    Meal.objects.create(name='Breakfast')
    Meal.objects.create(name='Lunch')
    Meal.objects.create(name='Dinner')
    Meal.objects.create(name='Snack')


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_meal_types),
    ]
