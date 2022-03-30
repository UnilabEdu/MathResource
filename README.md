# MathResource
ეს არის მათემატიკის პროექტის რეპოზიტორია

## Links
[Trello](https://trello.com/b/t6W3COYI/%E1%83%9B%E1%83%90%E1%83%97%E1%83%94%E1%83%9B%E1%83%90%E1%83%A2%E1%83%98%E1%83%99%E1%83%98%E1%83%A1-%E1%83%A0%E1%83%94%E1%83%A1%E1%83%A3%E1%83%A0%E1%83%A1%E1%83%98) / 
[Design](https://xd.adobe.com/view/e7ab836b-330d-44f9-9a4a-393a25ddbe72-b2f8/) / 
[Front Only Repo](https://lukinoo.github.io/math-resource/)

## Branch Structure

main branches: `deploy` | `develop` 

temporary branches: `front` | `back` [ from `develop` ]

- `deploy` - stable branch
- `develop` - working branch
- `front` - workspace for front-end division
- `back` - workspace for back-end division


### pull request
All the pull requests are sent to your `division` branch.  
When creating new branch, always use the structure of the branch anatomy.

branch anatomy: `division`/`type`/`title`

divisions: `front` | `back`

`division` branch is synced to the `development` branch once a week.



# გვერდები
ტექნიკურის ბმული: [https://bmuli.ge/gDxuusyI](https://bmuli.ge/gDxuusyI)

- მთავრი გვერდები: 
  - base
  - მთავრი გვერდი
  - კონტაქტი
  - პროექტის შესახებ
  - Error pages (ეს ცალკე ბლუპრინტია)
- მომხმარებლის გვერდები:
  - პირადი გვერდი (User Dashboard)
  - რეგისტრაცია [flask_user] `url_for('user.register') `
  - ავტორიზაცია [flask_user] `url_for('user.login')`
  - პაროლის აღდგენა [flask_user] `url_for('user.forgot_password')`
  - პროფილის გვერდი [flask_user] `url_for('user.profile')`
- დავალების გვერდები:
  - დეტალური გვერდი
  - ადმინის გვერდი [flask_admin]
