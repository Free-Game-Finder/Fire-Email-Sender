import requests
from scripts import db


free_game_url = 'https://raw.githubusercontent.com/Free-Game-Finder/Steam/main/data/free_game_data.json'


def get_store():
    return "steam"


def get_json(url):
    return requests.get(url, timeout=10).json()


def html_path():
    return "email.html"


def get_emails():
    return db.db_email_list(get_store())


def get_free_games():
    response = get_json(free_game_url)
    free_games = []
    for key, item in response.items():
        free_games.append(
            {
                "key": key,
                "name": item[key]["data"]["name"],
                "header_image": item[key]["data"]["header_image"],
                "detailed_description": item[key]["data"]["detailed_description"]
            }
        )
    return free_games


def add_to_html(html):

    free_games = get_free_games()

    insert_html = ""

    for game in free_games:

        insert_html += f"""
    <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%"
                                        class="templateContainer">
                                        <tr>
                                            <td valign="top" class="bodyContainer">
                                                <table class="mcnImageBlock" style="min-width:100%;" width="100%"
                                                    cellspacing="0" cellpadding="0" border="0">
                                                    <tbody class="mcnImageBlockOuter">
                                                        <tr>
                                                            <td style="padding:9px" class="mcnImageBlockInner" valign="top">
                                                                <table class="mcnImageContentContainer"
                                                                    style="min-width:100%;" width="100%" cellspacing="0"
                                                                    cellpadding="0" border="0" align="left">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td class="mcnImageContent"
                                                                                style="padding-right: 9px; padding-left: 9px; padding-top: 0; padding-bottom: 0; text-align:center;"
                                                                                valign="top">


                                                                                <img alt=""
                                                                                    src="{game['header_image']}"
                                                                                    style="max-width:564px; padding-bottom: 0; display: inline !important; vertical-align: bottom;"
                                                                                    class="mcnImage" width="564"
                                                                                    align="middle">


                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <table class="mcnTextBlock" style="min-width:100%;" width="100%"
                                                    cellspacing="0" cellpadding="0" border="0">
                                                    <tbody class="mcnTextBlockOuter">
                                                        <tr>
                                                            <td class="mcnTextBlockInner" style="padding-top:9px;"
                                                                valign="top">
                                                                <!--[if mso]>
                    <table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
                    <tr>
                    <![endif]-->

                                                                <!--[if mso]>
                    <td valign="top" width="600" style="width:600px;">
                    <![endif]-->
                                                                <table style="max-width:100%; min-width:100%;"
                                                                    class="mcnTextContentContainer" width="100%"
                                                                    cellspacing="0" cellpadding="0" border="0" align="left">
                                                                    <tbody>
                                                                        <tr>

                                                                            <td class="mcnTextContent"
                                                                                style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;"
                                                                                valign="top">

                                                                                <h3>{game['name']}</h3>
                                                                                <p>{game['detailed_description']}</p>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                                <!--[if mso]>
                    </td>
                    <![endif]-->

                                                                <!--[if mso]>
                    </tr>
                    </table>
                    <![endif]-->
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <table class="mcnButtonBlock" style="min-width:100%;" width="100%"
                                                    cellspacing="0" cellpadding="0" border="0">
                                                    <tbody class="mcnButtonBlockOuter">
                                                        <tr>
                                                            <td style="padding-top:0; padding-right:18px; padding-bottom:18px; padding-left:18px;"
                                                                class="mcnButtonBlockInner" valign="top" align="center">
                                                                <table class="mcnButtonContentContainer"
                                                                    style="border-collapse: separate !important;border-radius: 3px;background-color: #009FC7;"
                                                                    cellspacing="0" cellpadding="0" border="0">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td class="mcnButtonContent"
                                                                                style="font-family: Helvetica; font-size: 18px; padding: 18px;"
                                                                                valign="middle" align="center">
                                                                                <a class="mcnButton " title="Get It Here"
                                                                                    href="#" target="_blank"
                                                                                    style="font-weight: bold;letter-spacing: -0.5px;line-height: 100%;text-align: center;text-decoration: none;color: #FFFFFF;">
                                                                                    Get It Here</a>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <table class="mcnDividerBlock" style="min-width:100%;" width="100%"
                                                    cellspacing="0" cellpadding="0" border="0">
                                                    <tbody class="mcnDividerBlockOuter">
                                                        <tr>
                                                            <td class="mcnDividerBlockInner"
                                                                style="min-width:100%; padding:18px;">
                                                                <table class="mcnDividerContent" style="min-width:100%;"
                                                                    width="100%" cellspacing="0" cellpadding="0" border="0">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td>
                                                                                <span></span>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                                <!--            
                    <td class="mcnDividerBlockInner" style="padding: 18px;">
                    <hr class="mcnDividerContent" style="border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;" />
    -->
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>

                                            </td>
                                        </tr>
                                    </table>
        """

    return html.replace("[free_games]", insert_html)
