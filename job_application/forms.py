from django import forms
from .models import Job

    
class JobForm(forms.ModelForm):

    class Meta:
        model = Job
   
        fields = ('job_id', 'position_name', 'company_name','appl_submitted','status' )
        labels = {
            'company_name' : 'Company Name',
            'job_id' : 'Job ID',
            'position_name' : 'Position Name',
            'appl_submitted' : 'Date Submitted',
        }

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "Select"
        self.fields['status'].required = False


    