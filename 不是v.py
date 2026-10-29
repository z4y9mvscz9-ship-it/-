import json
import urllib.request
from urllib.parse import quote

CITY = "Zhuhai"

def fetch_weather(city_name: str):
    url = f"https://wttr.in/{quote(city_name)}?format=j1"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        text = resp.read().decode("utf-8")
        return json.loads(text)

def print_weather(data):
    current = data.get("current_condition", [{}])[0]
    weather_desc = current.get("weatherDesc", [{"value": "未知"}])[0].get("value", "未知")
    temp_c = current.get("temp_C", "-")
    feels_like = current.get("FeelsLikeC", "-")
    humidity = current.get("humidity", "-")
    wind_dir = current.get("winddir16Point", "-")
    wind_speed = current.get("windspeedKmph", "-")

    print("========================================")
    print(f"城市：{CITY}")
    print(f"天气：{weather_desc}")
    print(f"当前温度：{temp_c}°C")
    print(f"体感温度：{feels_like}°C")
    print(f"湿度：{humidity}%")
    print(f"风向：{wind_dir}")
    print(f"风速：{wind_speed} km/h")
    print("========================================")
    print("未来 3 天天气：")
    print()

    for day in data.get("weather", [])[:3]:
        date = day.get("date", "未知日期")
        maxtemp = day.get("maxtempC", "-")
        mintemp = day.get("mintempC", "-")
        desc = day.get("hourly", [{"weatherDesc": [{"value": "未知"}]}])[0].get("weatherDesc", [{"value": "未知"}])[0].get("value", "未知")
        print(f"{date}: {desc}，最低 {mintemp}°C，最高 {maxtemp}°C")

def main():
    try:
        data = fetch_weather(CITY)
        print_weather(data)
    except Exception as e:
        print("获取天气失败：")
        print(e)
        print("请检查网络连接，或稍后重试。")

if __name__ == "__main__":
    main()
