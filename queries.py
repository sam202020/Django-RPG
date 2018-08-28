1. from charactercreator.models import *
   Character.objects.count()
   302 Characters

2. 68 fighters, 108 Mages, 75 clerics, 51 thiefs, 11 necromancers(subclass of Mage) (same code)

3. from armory.models import *
   Item.objects.count()
   174

4. Weapon.objects.count()
   37
   Item.objects.count() - Weapon.objects.count()
   137

5. chr = Character.objects.all()
   arr = []
   for x in chr:
      arr.append(x.inventory.count())
   sum = 0
   for x in arr:
      sum += x
   sum / 302
   2.9735099337748343