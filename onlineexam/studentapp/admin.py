from django.contrib import admin
from .models import student
from .models import result,exam
from django.utils.safestring import mark_safe

class Student(admin.ModelAdmin):
    list_display = ('Fullname','Course')
                    
class Exam(admin.ModelAdmin):
    list_display = ('student_id','Course','Level','course_level_link')
    
    def course_level_link(self, obj):
     if obj.Course == 'python':
        if obj.Level == 'exam1':
            return mark_safe('<a href="https://colab.research.google.com/drive/1bwRvNKR4ajkbnKfXXwxu6NYs_zk6QHpw?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam2':
            return mark_safe('<a href="https://colab.research.google.com/drive/1Kp3veqo_ApZhIa2h49n0LKJxOsz9pBUL?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam3':
            return mark_safe('<a href="https://colab.research.google.com/drive/1a4MzeiSPWMdU3S-dFJyEoQ2zXedvl-px?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam4':
             return mark_safe('<a href="https://colab.research.google.com/drive/1c6I9-IPGdYiw0_JdnyqmDb8xb4ec9nD9?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam5':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam6':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam7':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam8':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam9':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam10':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam11':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam12':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam13':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam14':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam15':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        else:
            return 'Unknown'
        
     elif obj.Course == 'oops':
        if obj.Level == 'exam1':
            return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam2':
            return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam3':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam4':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam5':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam6':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam7':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam8':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam9':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam10':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam11':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam12':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam13':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam14':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        elif obj.Level == 'exam15':
             return mark_safe('<a href="https://colab.research.google.com/drive/1-w_a0QcSRcBXBnJ_V6WxoKDo8WOyX2zo?usp=sharing">ATTEND YOUR TEST HERE</a>')
        else:
            return 'Unknown'
            
    course_level_link.short_description = 'Link'

    def rendered_course_link(self, obj):
        return self.course_level_link(obj)
    rendered_course_link.allow_tags = True
    rendered_course_link.short_description = 'Course Link'

class Result(admin.ModelAdmin):
    list_display=('Fullname','download_result_link')    
    def download_result_link(self,obj):
        if obj.Result:
            return mark_safe(f'<a href="{obj.Result.url}" download>Download Result</a>')
        return "No Result"
    download_result_link.short_description = "Result"


admin.site.register(student,Student)
admin.site.register(result,Result)
admin.site.register(exam,Exam)