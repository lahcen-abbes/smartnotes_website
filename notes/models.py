from django.db import models
from django.contrib.auth.models import User  #zedna hadi
# Create your models here.
class Notes(models.Model): #hna notes wertet mel models.Model
    title = models.CharField(max_length=200) #title howa attribute w CharField te3ni chaine de charactères limited, max_length=200 te3ni title mayfotch 200 7erf
    text = models.TextField() #TextField te3ni chaine de charactères unlimited
    created = models.DateTimeField(auto_now_add=True) #We also want to know when this note was created(winta tecréat), auto_now_add=True me3netha winma necréo notes jdid tetecréa m3ah la date li tecréat fiha
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes") #zedna hada foreign key li howa fl asl a primary key ta3 another table li howa table ta3 users,User howa the model we want to create a link with(li howa table ta3 user), on_delete me3naha chaghadi yesralha had attribute kon tetsuprima mn table we7dakhor li rahi associated m3a table hada aya drna models.CASCADE w li me3nah if a user gets deleted, we also want to delete all the notes associated with them. related_name derna fiha ism model li rana dayrin fiha foreign key w li rana fiha w li hiya notes