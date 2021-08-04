

@api_view(["GET"])
def tweet_post(request):
    text = request.GET.get('text')
    consumer_key='(add consumer-key)'
    consumer_secret_key='(add consumer secret key)'
    access_token='(add access token)'
    access_token_secret='(add access token secret)'
    try:
        auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
        auth.set_access_token(access_token,access_token_secret)
        api=tweepy.API(auth)
        api.update_status(status=text)
        return Response({'status':True},status=status.HTTP_200_OK)
    except:
        return Response({'status':False},status=status.HTTP_400_BAD_REQUEST)

    
@api_view(["GET"])
def facebook_post(request):
    message = request.GET.get('message')
    link = request.GET.get('link')
    access_token = config('FACEBOOK_ACCESS_TOKEN', default = "")
    page_id = config('FACEBOOK_PAGE_ID', default = "")
    data = {'message':message,
        'link':link,
        'access_token':access_token}
    try:
        x = requests.post(url=f'https://graph.facebook.com/{page_id}/feed',data=data)
    except:
        return Response({'status':False},status=status.HTTP_400_BAD_REQUEST)
    if (x.status_code==200):
        return Response({'status':True},status=status.HTTP_200_OK) 
    return Response({'status':False},status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(["GET"])
def instagram_post(request):
    caption = request.GET.get('caption',"")
    image_url = request.GET.get('image_url',"")
    access_token = config('FACEBOOK_ACCESS_TOKEN', default = "")
    page_id = config('INSTAGRAM_PAGE_ID', default = "")
    data = {'image_url':image_url,
        'caption':caption,
        'access_token':access_token}
    try:
        x = requests.post(url=f'https://graph.facebook.com/{page_id}/media/',data=data)
    except:
        return Response({'status':False},status=status.HTTP_400_BAD_REQUEST)
    if(x.status_code==200):
        new_dict = x.json()
        new_data = {'creation_id':new_dict.get('id',""),'access_token':access_token}
        try:
            y = requests.post(url=f'https://graph.facebook.com/{page_id}/media_publish/',data=new_data)
        except:
            return Response({'status':False},status=status.HTTP_400_BAD_REQUEST)
        if(y.status_code==200):
            return Response({'status':True},status=status.HTTP_200_OK)
        else:
            return Response({'status':False},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'status':False},status=status.HTTP_400_BAD_REQUEST)
    
 

    
