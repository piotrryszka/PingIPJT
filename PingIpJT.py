import os

with open("ip_list.txt") as file:
    park = file.read()
    park = park.splitlines()
    print(f" {park}  \n")
    # ping and tracert for each ip in the file
for ip in park:
    response = os.popen(f"ping {ip} ").read()
    Traceroute = os.popen(f"tracert -d {ip}").read()
    # saving some ping output details to output file

    if ("Request timed out." or "unreachable") in response:
        print(response)
        print(Traceroute)
        f = open("ip_output.txt", "a")
        # f.write(str(ip) + ' link is down' + '\n')
        f.write(str(response) + '\n')
        f.write(str(Traceroute) + '\n')
        f.close()
    else:
        print(response)
        print(Traceroute)
        f = open("ip_output.txt", "a")
        # f.write(str(ip) + ' is up ' + '\n')
        f.write(str(response) + '\n')
        f.write(str(Traceroute) + '\n')
        f.close()
        # print output file to screen
with open("ip_output.txt") as file:
    output = file.read()
    f.close()
    print(output)
with open("ip_output.txt", "a") as file:
    pass
