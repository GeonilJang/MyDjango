from django.views.generic import View, TemplateView
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

class PostList1(View):  # 내가 만든 string html을 렌더할때
    def get(self, request):
        name ="공유"
        html = self.get_template_string().format(name=name)
        # html = """
        #         <h1>Hello Python with Django</h1>
        #         <p>{name}</p>
        #         <p>여러분의 친구가 되어 드리겠습니다.</p>
        #         """.format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return """
                    <h1>Hello Python with Django</h1>
                    <p>{name}</p>
                    <p>여러분의 친구가 되어 드리겠습니다.</p>
                """

post_list1 = PostList1.as_view()
# post_list2 = PostList1.as_view()

class PostList2(TemplateView): #template -> html을 렌더할 때
    template_name = 'dojo/post_list2.html'

    #템플릿에서 사용하고 있는 인자넘겨주는 방법
    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = "공유"
        return context


post_list2 = PostList2.as_view()

class PostList3(View):
    pass

class PostList4(View):
    pass
