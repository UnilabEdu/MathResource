# MathResource
ეს არის მათემატიკის პროექტის რეპოზიტორია


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
