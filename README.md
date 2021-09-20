# Caivy-Bot | Facebook Graph API 

A useful Facebook Graph API bot that can integrate with your facebook page to easily manage your page.



## Features

- Check if there is a comment made on the specify post
- Reply to the user that just commented
- Private Replies to user that commented


  
## Installation

Clone the project

```bash
  git clone https://github.com/Caivy/Glampoo-Bot.git
```
Go to the project directory

```bash
  cd Glampoo-Bot
```

Install dependencies

```bash
  pip install requirements.txt
```

Run the Bot

```bash
  python3 Glampoo.py
```

  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`Page_Access_Token`

`Page_ID`

`Post_ID`



## Permission Required

To run this project, you will need the following Permission

`pages_messaging` ADVANCE ACCESS REQUIRE

`pages_read_engagement`

`pages_manage_posts`


## API Reference

#### Get Comments

```http
  GET /v12.0/{object-id}/comments
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `summary` | `string` | A summary of metadata about the comments on the object. Importantly this metadata includes order which indicates how the comments are being sorted. |
| `filter` | `string` | This determines which comments are returned when comment replies are available. It can be either: toplevel or stream |

#### Field
An array of Comment objects in addition to the following fields when summary is true in the request.


```http
  GET /v12.0/{object-id}/comments?summary=1&order='reverse_chronological'
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `order` | `enum` | Order in which comments were returned. chronological and reverse_chronological |

For more information please refer to the Offical Facebook Graph API Doccumentation : https://developers.facebook.com/docs/graph-api/reference

  
## Demo

[![Caivy-Bot | Demo](https://img.youtube.com/vi/RP82pYR6tUE/0.jpg)](https://www.youtube.com/watch?v=RP82pYR6tUE "Caivy-Bot | Demo")

  
## Used By

This project is used by the following Pages:

- Glampoo
- Caivy Marketplace

  
## Authors

- [@Caivy](https://github.com/Caivy)

  
