from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets.views import snippet_list, snippet_detail
from snippets.views import SnippetList, SnippetDetail

urlpatterns = [
    # path('snippets/', snippet_list, name='snippet_list'),
    path('snippets/', SnippetList.as_view(), name='snippet_list'),
    # path('snippets/<int:pk>/', snippet_detail, name='snippet_detail'),
    path('snippets/<int:pk>/', SnippetDetail.as_view(), name='snippet_detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
