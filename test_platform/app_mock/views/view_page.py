from django.shortcuts import render
from app_mock.models import MockData
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def mock_list(request):
    search_uri = request.GET.get("searchURI", "")
    page_num = request.GET.get("page", "")

    if search_uri == "":
        data = MockData.objects.all().order_by('-create_time')
    else:
        data = MockData.objects.filter(uri__contains=search_uri)

    paginator = Paginator(data, 10)

    if page_num == "":
        page_num = 1

    try:
        contacts = paginator.page(page_num)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    page_data = {
        "number": contacts.number,
        "has_previous": contacts.has_previous,
        "previous_page_number": contacts.previous_page_number,
        "has_next": contacts.has_next,
        "next_page_number": contacts.next_page_number,
        "num_pages": contacts.paginator.num_pages
    }

    data_list = []
    for data in contacts:
        data_dict = {
            "id": data.id,
            "method": data.method,
            "uri": data.uri,
            "desc": data.desc,
        }
        data_list.append(data_dict)

    return render(request, "mock2.html", {"part": "list", "mockApi": data_list, "page": page_data, "uri": search_uri})


def mock_add(request, mid):
    return render(request, "mock_add2.html", {"part": "add"})
