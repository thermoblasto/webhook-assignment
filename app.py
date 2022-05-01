from flask import Flask, request, Response,json
import mysql.connector

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello, Docker!'
  
@app.route('/attribution', methods=['POST'])

def respond():
    data = request.json
    idfv=data["idfv"]
    device_category=data["device_category"]
    af_sub1=data["af_sub1"]
    customer_user_id=data["customer_user_id"]
    is_lat=data["is_lat"]
    contributor_2_af_prt=data["contributor_2_af_prt"]
    bundle_id=data["bundle_id"]
    gp_broadcast_referrer=data["gp_broadcast_referrer"]
    contributor_2_touch_time=data["contributor_2_touch_time"]
    contributor_3_touch_type=data["contributor_3_touch_type"]
    event_source=data["event_source"]
    af_cost_value=data["af_cost_value"]
    contributor_1_match_type=data["contributor_1_match_type"]
    app_version=data["app_version"]
    contributor_3_af_prt=data["contributor_3_af_prt"]
    custom_data=data["custom_data"]
    contributor_2_touch_type=data["contributor_2_touch_type"]
    gp_install_begin=data["gp_install_begin"]
    city=data["city"]
    amazon_aid=data["amazon_aid"]
    gp_referrer=data["gp_referrer"]
    af_cost_model=data["af_cost_model"]
    af_c_id=data["af_c_id"]
    attributed_touch_time_selected_timezone=data["attributed_touch_time_selected_timezone"]
    selected_currency=data["selected_currency"]
    app_name=data["app_name"]
    install_time_selected_timezone=data["install_time_selected_timezone"]
    postal_code=data["postal_code"]
    wifi=data["wifi"]
    install_time=data["install_time"]
    operator=data["operator"]
    attributed_touch_type=data["attributed_touch_type"]
    af_attribution_lookback=data["af_attribution_lookback"]
    keyword_match_type=data["keyword_match_type"]
    af_adset_id=data["af_adset_id"]
    device_download_time_selected_timezone=data["device_download_time_selected_timezone"]
    contributor_2_media_source=data["contributor_2_media_source"]
    contributor_2_match_type=data["contributor_2_match_type"]
    api_version=data["api_version"]
    attributed_touch_time=data["attributed_touch_time"]
    revenue_in_selected_currency=data["revenue_in_selected_currency"]
    is_retargeting=data["is_retargeting"]
    country_code=data["country_code"]
    gp_click_time=data["gp_click_time"]
    contributor_1_af_prt=data["contributor_1_af_prt"]
    match_type=data["match_type"]
    appsflyer_id=data["appsflyer_id"]
    dma=data["dma"]
    http_referrer=data["http_referrer"]
    af_sub5=data["af_sub5"]
    af_prt=data["af_prt"]
    event_revenue_currency=data["event_revenue_currency"]
    store_reinstall=data["store_reinstall"]
    install_app_store=data["install_app_store"]
    media_source=data["media_source"]
    deeplink_url=data["deeplink_url"]
    campaign=data["campaign"]
    af_keywords=data["af_keywords"]
    region=data["region"]
    cost_in_selected_currency=data["cost_in_selected_currency"]
    event_value=data["event_value"]
    ip=data["ip"]
    oaid=data["oaid"]
    event_time=data["event_time"]
    is_receipt_validated=data["is_receipt_validated"]
    contributor_1_campaign=data["contributor_1_campaign"]
    af_sub4=data["af_sub4"]
    imei=data["imei"]
    contributor_3_campaign=data["contributor_3_campaign"]
    event_revenue_usd=data["event_revenue_usd"]
    af_sub2=data["af_sub2"]
    original_url=data["original_url"]
    contributor_2_campaign=data["contributor_2_campaign"]
    android_id=data["android_id"]
    contributor_3_media_source=data["contributor_3_media_source"]
    af_adset=data["af_adset"]
    af_ad=data["af_ad"]
    state=data["state"]
    network_account_id=data["network_account_id"]
    device_type=data["device_type"]
    idfa=data["idfa"]
    retargeting_conversion_type=data["retargeting_conversion_type"]
    af_channel=data["af_channel"]
    af_cost_currency=data["af_cost_currency"]
    contributor_1_media_source=data["contributor_1_media_source"]
    keyword_id=data["keyword_id"]
    device_download_time=data["device_download_time"]
    contributor_1_touch_type=data["contributor_1_touch_type"]
    af_reengagement_window=data["af_reengagement_window"]
    af_siteid=data["af_siteid"]
    language=data["language"]
    app_id=data["app_id"]
    contributor_1_touch_time=data["contributor_1_touch_time"]
    event_revenue=data["event_revenue"]
    af_ad_type=data["af_ad_type"]
    carrier=data["carrier"]
    event_name=data["event_name"]
    af_sub_siteid=data["af_sub_siteid"]
    advertising_id=data["advertising_id"]
    os_version=data["os_version"]
    platform=data["platform"]
    af_sub3=data["af_sub3"]
    contributor_3_match_type=data["contributor_3_match_type"]
    selected_timezone=data["selected_timezone"]
    af_ad_id=data["af_ad_id"]
    contributor_3_touch_time=data["contributor_3_touch_time"]
    user_agent=data["user_agent"]
    is_primary_attribution=data["is_primary_attribution"]
    sdk_version=data["sdk_version"]
    event_time_selected_timezone=data["event_time_selected_timezone"]


    mydb = mysql.connector.connect(
       host="mysqldb",
       user="root",
       password="p@ssw0rd1",
       database="yousician"
     )
    cursor = mydb.cursor()
    cursor.execute(''' INSERT INTO attribution (device_category,af_sub1,customer_user_id,is_lat,contributor_2_af_prt,bundle_id,gp_broadcast_referrer,contributor_2_touch_time,contributor_3_touch_type,event_source,af_cost_value,contributor_1_match_type,app_version,contributor_3_af_prt,custom_data,contributor_2_touch_type,gp_install_begin,city,amazon_aid,gp_referrer,af_cost_model,af_c_id,attributed_touch_time_selected_timezone,selected_currency,app_name,install_time_selected_timezone,postal_code,wifi,install_time,operator,attributed_touch_type,af_attribution_lookback,keyword_match_type,af_adset_id,device_download_time_selected_timezone,contributor_2_media_source,contributor_2_match_type,api_version,attributed_touch_time,revenue_in_selected_currency,is_retargeting,country_code,gp_click_time,contributor_1_af_prt,match_type,appsflyer_id,dma,http_referrer,af_sub5,af_prt,event_revenue_currency,store_reinstall,install_app_store,media_source,deeplink_url,campaign,af_keywords,region,cost_in_selected_currency,event_value,ip,oaid,event_time,is_receipt_validated,contributor_1_campaign,af_sub4,imei,contributor_3_campaign,event_revenue_usd,af_sub2,original_url,contributor_2_campaign,contributor_3_media_source,af_adset,af_ad,state,network_account_id,device_type,retargeting_conversion_type,af_channel,af_cost_currency,contributor_1_media_source,keyword_id,device_download_time,contributor_1_touch_type,af_reengagement_window,af_siteid,language,app_id,contributor_1_touch_time,event_revenue,af_ad_type,carrier,event_name,af_sub_siteid,os_version,platform,af_sub3,contributor_3_match_type,selected_timezone,af_ad_id,contributor_3_touch_time,user_agent,is_primary_attribution,sdk_version,event_time_selected_timezone) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(device_category,af_sub1,customer_user_id,is_lat,contributor_2_af_prt,bundle_id,gp_broadcast_referrer,contributor_2_touch_time,contributor_3_touch_type,event_source,af_cost_value,contributor_1_match_type,app_version,contributor_3_af_prt,custom_data,contributor_2_touch_type,gp_install_begin,city,amazon_aid,gp_referrer,af_cost_model,af_c_id,attributed_touch_time_selected_timezone,selected_currency,app_name,install_time_selected_timezone,postal_code,wifi,install_time,operator,attributed_touch_type,af_attribution_lookback,keyword_match_type,af_adset_id,device_download_time_selected_timezone,contributor_2_media_source,contributor_2_match_type,api_version,attributed_touch_time,revenue_in_selected_currency,is_retargeting,country_code,gp_click_time,contributor_1_af_prt,match_type,appsflyer_id,dma,http_referrer,af_sub5,af_prt,event_revenue_currency,store_reinstall,install_app_store,media_source,deeplink_url,campaign,af_keywords,region,cost_in_selected_currency,event_value,ip,oaid,event_time,is_receipt_validated,contributor_1_campaign,af_sub4,imei,contributor_3_campaign,event_revenue_usd,af_sub2,original_url,contributor_2_campaign,contributor_3_media_source,af_adset,af_ad,state,network_account_id,device_type,retargeting_conversion_type,af_channel,af_cost_currency,contributor_1_media_source,keyword_id,device_download_time,contributor_1_touch_type,af_reengagement_window,af_siteid,language,app_id,contributor_1_touch_time,event_revenue,af_ad_type,carrier,event_name,af_sub_siteid,os_version,platform,af_sub3,contributor_3_match_type,selected_timezone,af_ad_id,contributor_3_touch_time,user_agent,is_primary_attribution,sdk_version,event_time_selected_timezone))
    cursor.execute(''' INSERT INTO attribution_identifier (idfv,idfa,advertising_id,android_id) VALUES(%s,%s,%s,%s)''',(idfv,idfa,advertising_id,android_id))
    mydb.commit()
    cursor.close()
    return Response(status=200)