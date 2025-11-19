"""
Django 框架广泛使用混合类来构建可重用的视图组件
"""
from django.core.exceptions import ImproperlyConfigured
from django.views import View
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404


# 模拟 Django 风格的混合类
class JSONResponseMixin:
    """返回 JSON 响应的混合类"""

    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context


class MultipleObjectMixin:
    """多对象操作的混合类"""

    model = None
    queryset = None

    def get_queryset(self):
        if self.queryset is not None:
            return self.queryset
        elif self.model is not None:
            return self.model.objects.all()
        else:
            raise ImproperlyConfigured("No model or queryset provided")

    def get_context_data(self, **kwargs):
        context = {}
        context['object_list'] = self.get_queryset()
        context.update(kwargs)
        return context


class SingleObjectMixin:
    """单对象操作的混合类"""

    model = None
    slug_field = 'slug'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.model.objects.all()

        # 模拟 get_object_or_404
        slug = self.kwargs.get('slug')
        if slug:
            obj = queryset.filter(**{self.slug_field: slug}).first()
            if obj:
                return obj
        raise Http404("Object not found")


# 具体视图类
class ProductListView(MultipleObjectMixin, JSONResponseMixin, View):
    """产品列表视图（返回 JSON）"""

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_json_response(context)


class ProductDetailView(SingleObjectMixin, JSONResponseMixin, View):
    """产品详情视图（返回 JSON）"""

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        context = {'product': obj}
        return self.render_to_json_response(context)


# 模拟使用
class MockProduct:
    """模拟产品模型"""
    objects = {
        'laptop': MockProduct('laptop', 'Gaming Laptop', 999.99),
        'phone': MockProduct('phone', 'Smart Phone', 499.99)
    }

    def __init__(self, slug, name, price):
        self.slug = slug
        self.name = name
        self.price = price

    @classmethod
    def all(cls):
        return list(cls.objects.values())


MockProduct.objects = MockProduct  # 简化模拟