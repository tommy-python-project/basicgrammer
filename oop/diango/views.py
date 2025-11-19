"""
视图 - 混合类的核心
"""
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from oop.diango.forms import CommentForm
from oop.diango.models import Article


class ArticleDetailView(FormMixin, DetailView):
    """
    这个视图结合了两个核心功能：
    1. DetailView: 负责获取 pk 对应的 Article 对象（self.object）并将其渲染到模版。
    2. FormMixin: 负责处理 CommentForm 的显示（GET）和提交（POST）
    """

    # --- DetailView 的配置
    model = Article
    template_name = 'diango/article_detail.html'
    context_object_name = 'article'  # 在模版中用{{ article }} 访问

    # --- FormMixin 的配置 ---
    form_class = CommentForm

    def get_success_url(self):
        """
        当表单（FormMixin）成功提交后，重定向到哪里
        我们重定向回到当前文章的详情页
        """
        return reverse_lazy('article-detail', kwargs={'pk': self.object.pk})

    # ---组合两个 Mixin 的核心逻辑 ---
    def get_context_data(self, **kwargs):
        """
        这个方法负责准备模版所需的数据
        """
        # 1. 调用super().get_context_data(**kwargs)
        #    - DetailView 的逻辑会添加 'article' (即 self.object)
        #    - FormMixin 的逻辑会添加 'form' (即 self.get_form())
        context = super().get_context_data(**kwargs)

        # 2. (额外)我们手动把这篇文章的所有评论也添加到上下文中
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        """
        当用户通过 POST 请求提交表单时，这个方法会被调用。
        DetailView 本身不处理 POST,所以我们使用FormMixin的逻辑。
        """
        # 1. 必须先调用 self.get_object() 来获取当前的文章对象 (self.object)
        #    这是 DetailView (继承自 SingleObjectMixin) 提供的功能。
        self.object = self.get_object()

        # 2. 获取表单实例，并填充 POST 数据
        #    这是 FormMixin 提供的功能。
        form = self.get_form()

        if form.is_valid():
            # 3. 如果表单有效，调用 form_valid
            #    这是 FormMixin 提供的功能。
            return self.form_valid(form)
        else:
            # 4. 如果表单无效，调用 form_invalid
            #    这是 FormMixin 提供的功能，它会重新渲染页面并显示错误。
            return self.form_invalid(form)

    def form_valid(self,form):
        """
        当表单验证通过时，FormMixin 会调用此方法。
        我们在这里重写它，以便在保存评论前，将其与当前文章和用户关联。
        """
        # 1. 从表单创建一个 comment 对象，但先不保存 (commit=False)
        comment = form.save(commit=False)


        # 2. 关联外键
        comment.article = self.object # self.object 是 DetailView 获取到的文章
        comment.author = self.request.user

        # 3. 保存到数据库
        comment.save()

        # 4. 调用父类的 form_valid,它会根据get_success_ur() 进行重定向
        return super().form_valid(form)