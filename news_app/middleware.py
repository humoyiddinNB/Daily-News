from django.shortcuts import render

class Custom502Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # 404 yoki 403 bo'lsa, 502 qaytarish
        if response.status_code in [403, 404]:
            return render(request, 'news/502.html', status=502)

        return response
