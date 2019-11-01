import csv
import requests

def get_repo_list():

    # change the Repositories 
    Repositories= 'android'
    api_url = 'https://api.github.com/orgs/%s/repos?per_page=100' % Repositories
    repos_list = []

    fields = ['name']
    repos = requests.get(api_url)
    for r in repos.json():
        repos_list.append([r[key] for key in fields])

    print("Repositeries List Created-")
    print(*repos_list,sep="\n")
    outp = open(('%s_repos.csv' % Repositories), 'w')
    writer = csv.writer(outp)
    writer.writerow(fields) # header
    writer.writerows(repos_list) # data
    outp.close()

    print("File written: %s" % ('%s_repos.csv' % Repositories))
    print("done")

if __name__ == "__main__":
    get_repo_list()
