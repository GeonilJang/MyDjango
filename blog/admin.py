from django.contrib import admin
from .models import Post, Comment, Tag

from django.utils.safestring import mark_safe

# Register your models here.
# admin.site.register(Post)


# #등록법 1
# admin.site.register(Post) @model만 등록하는 방법
#
# #등록법 2
# class PostAdmin(admin, ModelAdmin):
#     list_display= ['id','title','content'] #해당 어드민 페이지에서 값을 보여주고 싶을때
# admin.site.register(Post, PostAdmin) @model + 화면에 보여주고 싶은 클래스 같이 등록
#
# #등록법 3 : 장식자 형태로 지원
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','status','content_size','feeling','updated_at']
    list_display_links = ['title']
    list_editale = ['title']
    list_per_page = 100

    actions = ['delete_selected_post','make_published','make_Draft','make_withdraw','geonil_good','geonil_sad','geonil_bad'] #d여기에 등록 2018-06-28

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = "글자수"
    # content_size.allow_tags = True


    # geonil.allow_tags = True --->mark_safe 를 사용한 방법을 권장합니다.

    #여기서의 쿼리셋은 선택한 현재의 row 값만을 많한다.
    def delete_selected_post(self, request, queryset):
        updated_count = queryset.delete()
        self.message_user(request, '{}건 삭제'.format(updated_count[0]))
    delete_selected_post.short_description ="삭제"

    def make_published(self, request, queryset): #admin에서 목록에 해당하는 작업을 한번에 실행 처리
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}건 published'.format(updated_count))
    make_published.short_description = '지정 포스팅을 Published상태로 변경' # 함수의 이름으로 적용된 곳에 설명으로적용

    def make_Draft(self, request, queryset): #admin에서 목록에 해당하는 작업을 한번에 실행 처리
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건 Draft'.format(updated_count))
    make_Draft.short_description = '지정 포스팅을 Draft 상태로 변경'

    def make_withdraw(self, request, queryset): #admin에서 목록에 해당하는 작업을 한번에 실행 처리
        updated_count = queryset.update(status='w')
        self.message_user(request, '{}건 Withdraw'.format(updated_count))
    make_withdraw.short_description = '지정 포스팅을 Withdraw 상태로 변경'

    def geonil_good(self, request, qeuryset):
        updated_count = qeuryset.update(feeling='g')
        self.message_user(request, '{}건 좋음'.format(updated_count))
    geonil_good.short_description = '좋음'

    def geonil_sad(self, request, qeuryset):
        updated_count = qeuryset.update(feeling='s')
        self.message_user(request, '{}건 슬픔'.format(updated_count))
    geonil_sad.short_description = '슬픔'

    def geonil_bad(self, request, qeuryset):
        updated_count = qeuryset.update(feeling='b')
        self.message_user(request, '{}건 나쁨'.format(updated_count))
    geonil_bad.short_description = '나쁨'


    # def geonil_test(self, request, qeuryset):
    #     updated_count = qeuryset.update(title='제목2')
    #     self.message_user(request, '{}건 변경'.format(updated_count))
    # geonil_test.short_description = '제목변경'






##########comments 등록
@admin.register(Comment)
class CommetAdmin(admin.ModelAdmin):
    list_display = ['id','author','message','update_at']
    list_display_links = ['message']
    actions = ['delete_selected_post']
    def delete_selected_post(self, request, queryset):
        updated_count = queryset.delete()
        self.message_user(request, '{}건 삭제'.format(updated_count[0]))
    delete_selected_post.short_description ="삭제"





@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    
