import requests

# API key cho Google Custom Search API
google_api_key = "AIzaSyBVMrvMqDLmuWWJTu6UHGElrQ_Gf-96TzQ"
google_cx = "497846069748-t9903s9ur36nrlla9hgi2ulbb5fvt9md.apps.googleusercontent.com"

# Hàm để tìm kiếm với Google Custom Search API
def google_search(query, api_key, cx):
    url = "https://www.googleapis.com/customsearch/v1/siterestrict?key=AIzaSyBVMrvMqDLmuWWJTu6UHGElrQ_Gf-96TzQ&cx=017576662512468239146omuauf_lfve&q=cars&callback=hndlr"
    params = {
        'q': query,
        'key': api_key,
        'cx': cx
    }
    response = requests.get(url, params=params)

    # Kiểm tra mã trạng thái của phản hồi
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            print("Không thể giải mã JSON từ phản hồi.")
            return None
    else:
        print(f"Lỗi HTTP {response.status_code}: {response.text}")
        return None

# Truy vấn tìm kiếm
query = "Clown fish"
results = google_search(query, google_api_key, google_cx)

# Xử lý kết quả
if results and 'items' in results:
    for item in results['items']:
        title = item.get('title')
        snippet = item.get('snippet')
        link = item.get('link')
        print(f"Title: {title}\nSnippet: {snippet}\nLink: {link}\n")
else:
    print("No results found or there was an error.")