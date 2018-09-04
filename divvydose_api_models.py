import requests

totalModel = {
    'GitHub-User-PublicRepos': requests.get('https://api.github.com/users/kennethreitz').json()['public_repos'],
    'GitHub-User-Forks': requests.get('https://api.github.com/repos/kennethreitz/requests/forks').json(),
    'BitBucket-User-PublicRepos': len(requests.get('https://api.bitbucket.org/2.0/users/mailchimp/repositories').json()),
    'BitBucket-User-Forks': requests.get('https://api.bitbucket.org/2.0/repositories/mailchimp/mailchimp-api-python/forks').json()
}

watcherModel = {
    'GitHub-Watchers-count': len(requests.get('https://api.github.com/users/kennethreitz/followers').json()),
    'GitHub-Watchers-full': requests.get('https://api.github.com/users/kennethreitz/followers').json(),
    'BitBucket-Watchers-full': requests.get('https://api.bitbucket.org/2.0/users/mailchimp/followers').json()
}

starsModel = {
    'GitHub-Stars-full': requests.get('https://api.github.com/users/kennethreitz/starred').json(),
    'BitBucket-Stars-Full': requests.get('https://api.bitbucket.org/2.0/users/mailchimp/repositories')
}

issuesModel = {
    'GitHub-OpenIssues-full': requests.get('https://api.github.com/users/kennethreitz/requests/issues').json(),
    'BitBucket-OpenIssues-full': requests.get('https://api.bitbucket.org/2.0/repositories/mailchimp/mailchimp-api-python/issues')
}

commitsModel = {
    'GitHub-Repos-count': len(requests.get('https://api.github.com/repos/kennethreitz/requests/commits').json()),
    'GitHub-Repos-full': requests.get('https://api.github.com/repos/kennethreitz/requests/commits').json(),
    'BitBucket-Commits-count': len(requests.get('https://api.bitbucket.org/2.0/repositories/mailchimp/mailchimp-api-python/commits').json()),
    'BitBucket-Commits-full': requests.get('https://api.bitbucket.org/2.0/repositories/mailchimp/mailchimp-api-python/commits').json()
}

languagesModel = {
    'GitHub-Languages-Used-RequestsRepo': len(requests.get('https://api.github.com/repos/kennethreitz/requests/languages').json()),
    'BitBucket-Languages-Used': 'Not available at this time. Check back later.'
}