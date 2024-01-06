import requests
from bs4 import BeautifulSoup
import os
import jsonpath
import json
from lxml import etree
from translate import google_translate
from pdfgraph import Graphs
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
import re

urlstr = "https://medium.com/_/graphql"

#登录并获取coockie，待完善
def signIn(user, passwd):
    #todo 如果没登录，则登录
    header = {
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }

    # header = formulate_head(headerStr)
    response = requests.get(urlstr, headers=header)
    coockie = response.cookies.get_dict()
    print(coockie)
    print(response.status_code)
    pass

 
def formulate_head(headstr):
    header_lines_value = ''
    headerStr = headstr
    header_lines = headerStr.strip().split('\n')
 
    # print(header_lines)
    # exit()
    ret = ""
    jump = 0
    for i in range(jump,len(header_lines)):
        if i >= jump:
            if header_lines[i].rfind(':') != -1:
                ret += '\'' + header_lines[i] + ' ' + header_lines[i+1] + '\'' + ',\n'
                jump = i+2
    ret = re.sub(": ", "': '", ret)
    ret = ret[:-2]
    print(ret)
    return ret
 

def findFirst10():
    #暂未实现登录获取coockie，使用固定coockie，存在过期问题
    header = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "apollographql-client-name": "lite",
        "apollographql-client-version": "main-20240105-143320-f2439d8bbc",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
'Cookie':
'_gid=GA1.2.1715801314.1704508288; lightstep_guid/medium-web=86b944966d6599; lightstep_session_id=c203aca9fa47675b; pr=1.5; tz=-480; sz=822; uid=e69db1874c73; sid=1:po9nZloOV1NPBcpocxOyqLorBzdzAC7IfrGT9b9ihnyIJLwJ/MH9/VV9hsunphvl; xsrf=0ThU7mS2DQKkruEv; _ga=GA1.1.278949555.1704504106; __stripe_mid=f1cb0658-f7c0-42a2-b042-c312611bc883d9c502; _dd_s=rum=0&expire=1704550591006; _ga_7JY7T788PK=GS1.1.1704546725.7.1.1704549691.0.0.0',        "graphql-operation": "WebInlineTopicFeedQuery",
        "Host": "medium.com",
        "medium-frontend-app": "lite/main-20240105-143320-f2439d8bbc",
        "medium-frontend-path": "/?tag=software-engineering",
        "medium-frontend-route": "homepage",
        "Origin": "https://medium.com",
        "ot-tracer-sampled": "true",
        "ot-tracer-spanid": "2d36c2cf1b55e26a",
        "ot-tracer-traceid": "76a57d81662b98ec",
        "Referer": "https://medium.com/?tag=software-engineering",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15"
    }
    data = {
    "operationName": "WebInlineTopicFeedQuery",
    "variables": {
      "tagSlug": "software-engineering",
      "paging": {
        "to": "10",
        "from": "5",
        "limit": 5,
        "source": "30f33df2-da3c-45f8-b154-9e9a6e04b381"
      },
      "skipCache": True
    },
    "query": "query WebInlineTopicFeedQuery($tagSlug: String!, $paging: PagingOptions!, $skipCache: Boolean) {\n  personalisedTagFeed(tagSlug: $tagSlug, paging: $paging, skipCache: $skipCache) {\n    items {\n      ... on TagFeedItem {\n        feedId\n        reason\n        moduleSourceEncoding\n        post {\n          ...PostPreview_post\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    pagingInfo {\n      next {\n        source\n        limit\n        from\n        to\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PostPreview_post on Post {\n  id\n  creator {\n    ...PostPreview_user\n    __typename\n    id\n  }\n  collection {\n    ...CardByline_collection\n    ...ExpandablePostByline_collection\n    __typename\n    id\n  }\n  ...InteractivePostBody_postPreview\n  firstPublishedAt\n  isLocked\n  isSeries\n  latestPublishedAt\n  inResponseToCatalogResult {\n    __typename\n  }\n  pinnedAt\n  pinnedByCreatorAt\n  previewImage {\n    id\n    focusPercentX\n    focusPercentY\n    __typename\n  }\n  readingTime\n  sequence {\n    slug\n    __typename\n  }\n  title\n  uniqueSlug\n  ...CardByline_post\n  ...PostFooterActionsBar_post\n  ...InResponseToEntityPreview_post\n  ...PostScrollTracker_post\n  ...HighDensityPreview_post\n  __typename\n}\n\nfragment PostPreview_user on User {\n  __typename\n  name\n  username\n  ...CardByline_user\n  ...ExpandablePostByline_user\n  id\n}\n\nfragment CardByline_user on User {\n  __typename\n  id\n  name\n  username\n  mediumMemberAt\n  socialStats {\n    followerCount\n    __typename\n  }\n  ...useIsVerifiedBookAuthor_user\n  ...userUrl_user\n  ...UserMentionTooltip_user\n}\n\nfragment useIsVerifiedBookAuthor_user on User {\n  verifications {\n    isBookAuthor\n    __typename\n  }\n  __typename\n  id\n}\n\nfragment userUrl_user on User {\n  __typename\n  id\n  customDomainState {\n    live {\n      domain\n      __typename\n    }\n    __typename\n  }\n  hasSubdomain\n  username\n}\n\nfragment UserMentionTooltip_user on User {\n  id\n  name\n  username\n  bio\n  imageId\n  mediumMemberAt\n  membership {\n    tier\n    __typename\n    id\n  }\n  ...UserAvatar_user\n  ...UserFollowButton_user\n  ...useIsVerifiedBookAuthor_user\n  __typename\n}\n\nfragment UserAvatar_user on User {\n  __typename\n  id\n  imageId\n  mediumMemberAt\n  membership {\n    tier\n    __typename\n    id\n  }\n  name\n  username\n  ...userUrl_user\n}\n\nfragment UserFollowButton_user on User {\n  ...UserFollowButtonSignedIn_user\n  ...UserFollowButtonSignedOut_user\n  __typename\n  id\n}\n\nfragment UserFollowButtonSignedIn_user on User {\n  id\n  name\n  __typename\n}\n\nfragment UserFollowButtonSignedOut_user on User {\n  id\n  ...SusiClickable_user\n  __typename\n}\n\nfragment SusiClickable_user on User {\n  ...SusiContainer_user\n  __typename\n  id\n}\n\nfragment SusiContainer_user on User {\n  ...SignInOptions_user\n  ...SignUpOptions_user\n  __typename\n  id\n}\n\nfragment SignInOptions_user on User {\n  id\n  name\n  __typename\n}\n\nfragment SignUpOptions_user on User {\n  id\n  name\n  __typename\n}\n\nfragment ExpandablePostByline_user on User {\n  __typename\n  id\n  name\n  imageId\n  ...userUrl_user\n  ...useIsVerifiedBookAuthor_user\n}\n\nfragment CardByline_collection on Collection {\n  name\n  ...collectionUrl_collection\n  __typename\n  id\n}\n\nfragment collectionUrl_collection on Collection {\n  id\n  domain\n  slug\n  __typename\n}\n\nfragment ExpandablePostByline_collection on Collection {\n  __typename\n  id\n  name\n  domain\n  slug\n}\n\nfragment InteractivePostBody_postPreview on Post {\n  extendedPreviewContent(\n    truncationConfig: {previewParagraphsWordCountThreshold: 400, minimumWordLengthForTruncation: 150, truncateAtEndOfSentence: true, showFullImageCaptions: true, shortformPreviewParagraphsWordCountThreshold: 30, shortformMinimumWordLengthForTruncation: 30}\n  ) {\n    bodyModel {\n      ...PostBody_bodyModel\n      __typename\n    }\n    isFullContent\n    __typename\n  }\n  __typename\n  id\n}\n\nfragment PostBody_bodyModel on RichText {\n  sections {\n    name\n    startIndex\n    textLayout\n    imageLayout\n    backgroundImage {\n      id\n      originalHeight\n      originalWidth\n      __typename\n    }\n    videoLayout\n    backgroundVideo {\n      videoId\n      originalHeight\n      originalWidth\n      previewImageId\n      __typename\n    }\n    __typename\n  }\n  paragraphs {\n    id\n    ...PostBodySection_paragraph\n    __typename\n  }\n  ...normalizedBodyModel_richText\n  __typename\n}\n\nfragment PostBodySection_paragraph on Paragraph {\n  name\n  ...PostBodyParagraph_paragraph\n  __typename\n  id\n}\n\nfragment PostBodyParagraph_paragraph on Paragraph {\n  name\n  type\n  ...ImageParagraph_paragraph\n  ...TextParagraph_paragraph\n  ...IframeParagraph_paragraph\n  ...MixtapeParagraph_paragraph\n  ...CodeBlockParagraph_paragraph\n  __typename\n  id\n}\n\nfragment ImageParagraph_paragraph on Paragraph {\n  href\n  layout\n  metadata {\n    id\n    originalHeight\n    originalWidth\n    focusPercentX\n    focusPercentY\n    alt\n    __typename\n  }\n  ...Markups_paragraph\n  ...ParagraphRefsMapContext_paragraph\n  ...PostAnnotationsMarker_paragraph\n  __typename\n  id\n}\n\nfragment Markups_paragraph on Paragraph {\n  name\n  text\n  hasDropCap\n  dropCapImage {\n    ...MarkupNode_data_dropCapImage\n    __typename\n    id\n  }\n  markups {\n    ...Markups_markup\n    __typename\n  }\n  __typename\n  id\n}\n\nfragment MarkupNode_data_dropCapImage on ImageMetadata {\n  ...DropCap_image\n  __typename\n  id\n}\n\nfragment DropCap_image on ImageMetadata {\n  id\n  originalHeight\n  originalWidth\n  __typename\n}\n\nfragment Markups_markup on Markup {\n  type\n  start\n  end\n  href\n  anchorType\n  userId\n  linkMetadata {\n    httpStatus\n    __typename\n  }\n  __typename\n}\n\nfragment ParagraphRefsMapContext_paragraph on Paragraph {\n  id\n  name\n  text\n  __typename\n}\n\nfragment PostAnnotationsMarker_paragraph on Paragraph {\n  ...PostViewNoteCard_paragraph\n  __typename\n  id\n}\n\nfragment PostViewNoteCard_paragraph on Paragraph {\n  name\n  __typename\n  id\n}\n\nfragment TextParagraph_paragraph on Paragraph {\n  type\n  hasDropCap\n  codeBlockMetadata {\n    mode\n    lang\n    __typename\n  }\n  ...Markups_paragraph\n  ...ParagraphRefsMapContext_paragraph\n  __typename\n  id\n}\n\nfragment IframeParagraph_paragraph on Paragraph {\n  type\n  iframe {\n    mediaResource {\n      id\n      iframeSrc\n      iframeHeight\n      iframeWidth\n      title\n      __typename\n    }\n    __typename\n  }\n  layout\n  ...Markups_paragraph\n  __typename\n  id\n}\n\nfragment MixtapeParagraph_paragraph on Paragraph {\n  type\n  mixtapeMetadata {\n    href\n    mediaResource {\n      mediumCatalog {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  ...GenericMixtapeParagraph_paragraph\n  __typename\n  id\n}\n\nfragment GenericMixtapeParagraph_paragraph on Paragraph {\n  text\n  mixtapeMetadata {\n    href\n    thumbnailImageId\n    __typename\n  }\n  markups {\n    start\n    end\n    type\n    href\n    __typename\n  }\n  __typename\n  id\n}\n\nfragment CodeBlockParagraph_paragraph on Paragraph {\n  codeBlockMetadata {\n    lang\n    mode\n    __typename\n  }\n  __typename\n  id\n}\n\nfragment normalizedBodyModel_richText on RichText {\n  paragraphs {\n    ...normalizedBodyModel_richText_paragraphs\n    __typename\n  }\n  sections {\n    startIndex\n    ...getSectionEndIndex_section\n    __typename\n  }\n  ...getParagraphStyles_richText\n  ...getParagraphSpaces_richText\n  __typename\n}\n\nfragment normalizedBodyModel_richText_paragraphs on Paragraph {\n  markups {\n    ...normalizedBodyModel_richText_paragraphs_markups\n    __typename\n  }\n  codeBlockMetadata {\n    lang\n    mode\n    __typename\n  }\n  ...getParagraphHighlights_paragraph\n  ...getParagraphPrivateNotes_paragraph\n  __typename\n  id\n}\n\nfragment normalizedBodyModel_richText_paragraphs_markups on Markup {\n  type\n  __typename\n}\n\nfragment getParagraphHighlights_paragraph on Paragraph {\n  name\n  __typename\n  id\n}\n\nfragment getParagraphPrivateNotes_paragraph on Paragraph {\n  name\n  __typename\n  id\n}\n\nfragment getSectionEndIndex_section on Section {\n  startIndex\n  __typename\n}\n\nfragment getParagraphStyles_richText on RichText {\n  paragraphs {\n    text\n    type\n    __typename\n  }\n  sections {\n    ...getSectionEndIndex_section\n    __typename\n  }\n  __typename\n}\n\nfragment getParagraphSpaces_richText on RichText {\n  paragraphs {\n    layout\n    metadata {\n      originalHeight\n      originalWidth\n      id\n      __typename\n    }\n    type\n    ...paragraphExtendsImageGrid_paragraph\n    __typename\n  }\n  ...getSeriesParagraphTopSpacings_richText\n  ...getPostParagraphTopSpacings_richText\n  __typename\n}\n\nfragment paragraphExtendsImageGrid_paragraph on Paragraph {\n  layout\n  type\n  __typename\n  id\n}\n\nfragment getSeriesParagraphTopSpacings_richText on RichText {\n  paragraphs {\n    id\n    __typename\n  }\n  sections {\n    ...getSectionEndIndex_section\n    __typename\n  }\n  __typename\n}\n\nfragment getPostParagraphTopSpacings_richText on RichText {\n  paragraphs {\n    type\n    layout\n    text\n    codeBlockMetadata {\n      lang\n      mode\n      __typename\n    }\n    __typename\n  }\n  sections {\n    ...getSectionEndIndex_section\n    __typename\n  }\n  __typename\n}\n\nfragment CardByline_post on Post {\n  ...DraftStatus_post\n  ...Star_post\n  ...shouldShowPublishedInStatus_post\n  __typename\n  id\n}\n\nfragment DraftStatus_post on Post {\n  id\n  pendingCollection {\n    id\n    creator {\n      id\n      __typename\n    }\n    ...BoldCollectionName_collection\n    __typename\n  }\n  statusForCollection\n  creator {\n    id\n    __typename\n  }\n  isPublished\n  __typename\n}\n\nfragment BoldCollectionName_collection on Collection {\n  id\n  name\n  __typename\n}\n\nfragment Star_post on Post {\n  id\n  creator {\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment shouldShowPublishedInStatus_post on Post {\n  statusForCollection\n  isPublished\n  __typename\n  id\n}\n\nfragment PostFooterActionsBar_post on Post {\n  id\n  visibility\n  allowResponses\n  postResponses {\n    count\n    __typename\n  }\n  isLimitedState\n  creator {\n    id\n    __typename\n  }\n  collection {\n    id\n    __typename\n  }\n  ...MultiVote_post\n  ...PostSharePopover_post\n  ...OverflowMenuButtonWithNegativeSignal_post\n  ...PostPageBookmarkButton_post\n  __typename\n}\n\nfragment MultiVote_post on Post {\n  id\n  creator {\n    id\n    ...SusiClickable_user\n    __typename\n  }\n  isPublished\n  ...SusiClickable_post\n  collection {\n    id\n    slug\n    __typename\n  }\n  isLimitedState\n  ...MultiVoteCount_post\n  __typename\n}\n\nfragment SusiClickable_post on Post {\n  id\n  mediumUrl\n  ...SusiContainer_post\n  __typename\n}\n\nfragment SusiContainer_post on Post {\n  id\n  __typename\n}\n\nfragment MultiVoteCount_post on Post {\n  id\n  __typename\n}\n\nfragment PostSharePopover_post on Post {\n  id\n  mediumUrl\n  title\n  isPublished\n  isLocked\n  ...usePostUrl_post\n  ...FriendLink_post\n  __typename\n}\n\nfragment usePostUrl_post on Post {\n  id\n  creator {\n    ...userUrl_user\n    __typename\n    id\n  }\n  collection {\n    id\n    domain\n    slug\n    __typename\n  }\n  isSeries\n  mediumUrl\n  sequence {\n    slug\n    __typename\n  }\n  uniqueSlug\n  __typename\n}\n\nfragment FriendLink_post on Post {\n  id\n  ...SusiClickable_post\n  ...useCopyFriendLink_post\n  ...UpsellClickable_post\n  __typename\n}\n\nfragment useCopyFriendLink_post on Post {\n  ...usePostUrl_post\n  __typename\n  id\n}\n\nfragment UpsellClickable_post on Post {\n  id\n  collection {\n    id\n    __typename\n  }\n  sequence {\n    sequenceId\n    __typename\n  }\n  creator {\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment OverflowMenuButtonWithNegativeSignal_post on Post {\n  id\n  visibility\n  ...OverflowMenuWithNegativeSignal_post\n  __typename\n}\n\nfragment OverflowMenuWithNegativeSignal_post on Post {\n  id\n  creator {\n    id\n    __typename\n  }\n  collection {\n    id\n    __typename\n  }\n  ...OverflowMenuItemUndoClaps_post\n  ...AddToCatalogBase_post\n  __typename\n}\n\nfragment OverflowMenuItemUndoClaps_post on Post {\n  id\n  clapCount\n  ...ClapMutation_post\n  __typename\n}\n\nfragment ClapMutation_post on Post {\n  __typename\n  id\n  clapCount\n  ...MultiVoteCount_post\n}\n\nfragment AddToCatalogBase_post on Post {\n  id\n  isPublished\n  __typename\n}\n\nfragment PostPageBookmarkButton_post on Post {\n  ...AddToCatalogBookmarkButton_post\n  __typename\n  id\n}\n\nfragment AddToCatalogBookmarkButton_post on Post {\n  ...AddToCatalogBase_post\n  __typename\n  id\n}\n\nfragment InResponseToEntityPreview_post on Post {\n  id\n  inResponseToEntityType\n  __typename\n}\n\nfragment PostScrollTracker_post on Post {\n  id\n  collection {\n    id\n    __typename\n  }\n  sequence {\n    sequenceId\n    __typename\n  }\n  __typename\n}\n\nfragment HighDensityPreview_post on Post {\n  id\n  title\n  previewImage {\n    id\n    focusPercentX\n    focusPercentY\n    __typename\n  }\n  extendedPreviewContent(\n    truncationConfig: {previewParagraphsWordCountThreshold: 400, minimumWordLengthForTruncation: 150, truncateAtEndOfSentence: true, showFullImageCaptions: true, shortformPreviewParagraphsWordCountThreshold: 30, shortformMinimumWordLengthForTruncation: 30}\n  ) {\n    subtitle\n    __typename\n  }\n  ...HighDensityFooter_post\n  __typename\n}\n\nfragment HighDensityFooter_post on Post {\n  id\n  readingTime\n  tags {\n    ...TopicPill_tag\n    __typename\n  }\n  ...BookmarkButton_post\n  ...ExpandablePostCardOverflowButton_post\n  ...OverflowMenuButtonWithNegativeSignal_post\n  __typename\n}\n\nfragment TopicPill_tag on Tag {\n  __typename\n  id\n  displayTitle\n  normalizedTagSlug\n}\n\nfragment BookmarkButton_post on Post {\n  visibility\n  ...SusiClickable_post\n  ...AddToCatalogBookmarkButton_post\n  __typename\n  id\n}\n\nfragment ExpandablePostCardOverflowButton_post on Post {\n  creator {\n    id\n    __typename\n  }\n  ...ExpandablePostCardReaderButton_post\n  __typename\n  id\n}\n\nfragment ExpandablePostCardReaderButton_post on Post {\n  id\n  collection {\n    id\n    __typename\n  }\n  creator {\n    id\n    __typename\n  }\n  clapCount\n  ...ClapMutation_post\n  __typename\n}\n"
  }

    result = {}

    for i in range(1,21):#此处待优化，寻找所有文章中的top10，限制在100个主题里面找top10
        if i % 10 == 0:
            print(i)
        response = requests.post(urlstr, headers=header, json=data)
        # print(response.status_code)
        recvData = response.json()

        if jsonpath.jsonpath(recvData, '$.data.personalisedTagFeed.items'):
            items = jsonpath.jsonpath(recvData, '$.data.personalisedTagFeed.items.*')
            # with open('output.json', 'w') as f:
            #     json.dump(items,f)
            for item in items:
                # print(jsonpath.jsonpath(items[i]))
                clapCount = jsonpath.jsonpath(item, '$.post.clapCount')
                midUrl = jsonpath.jsonpath(item, '$.post.mediumUrl')
                if i > 2:   #第二遍循环的时候，总个数超过10，填一个就要删除一个
                    minValue = min(result.values())
                    if minValue < clapCount[0]:
                        for key in result.keys():
                            if result[key] == minValue:
                                del result[key]
                                break
                        result[midUrl[0]] = clapCount[0]
                else:
                    result[midUrl[0]] = clapCount[0]
        if jsonpath.jsonpath(recvData, '$.data.personalisedTagFeed.pagingInfo.next'):
            next = jsonpath.jsonpath(recvData, '$.data.personalisedTagFeed.pagingInfo.next')
            # print(next[0]['from'])
            data['variables']['paging']['from'] = next[0]['from']
            data['variables']['paging']['to'] = next[0]['to']

    return result

def retrieveFile(urlList):
    header = {'Accept':
'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding':
'gzip, deflate, br',
'Accept-Language':
'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Cache-Control':
'max-age=0',
'Cookie':
'_gid=GA1.2.1715801314.1704508288; lightstep_guid/medium-web=86b944966d6599; lightstep_session_id=c203aca9fa47675b; pr=1.5; tz=-480; sz=822; uid=e69db1874c73; sid=1:po9nZloOV1NPBcpocxOyqLorBzdzAC7IfrGT9b9ihnyIJLwJ/MH9/VV9hsunphvl; xsrf=0ThU7mS2DQKkruEv; _ga=GA1.1.278949555.1704504106; __stripe_mid=f1cb0658-f7c0-42a2-b042-c312611bc883d9c502; _dd_s=rum=0&expire=1704550591006; _ga_7JY7T788PK=GS1.1.1704546725.7.1.1704549691.0.0.0',        "graphql-operation": "WebInlineTopicFeedQuery",
'Sec-Ch-Ua':
'"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
'Sec-Ch-Ua-Mobile':
'?0',
'Sec-Ch-Ua-Platform':
'"Windows"',
'Sec-Fetch-Dest':
'document',
'Sec-Fetch-Mode':
'navigate',
'Sec-Fetch-Site':
'none',
'Sec-Fetch-User':
'?1',
'Upgrade-Insecure-Requests':
'1',
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
    resultList = []
    for url in urlList:
        print(url)
        response = requests.get(url, headers=header)
        content = response.text
        resultList.append(content)
        # break#for test
    return resultList

#解析返回的html报文似乎可以改为配置的方式，能匹配更多报文类型，待优化
#或者寻找一种可以直接保留html页面布局的方式，只翻译相应文字，并将翻译结果放入原始html文件
#这个方法尝试了一下，失败了，可能要花更多时间
def genPdf(contentList):
    for content in contentList:
        text = list()
        soup = BeautifulSoup(content, 'lxml')
        title = ''

        #鉴于全部html内容容易凌乱，只取article中的部分内容
        article = soup.find('article')
        soup1 = BeautifulSoup(str(article), 'lxml')

        for p in soup1.find_all(['h1', 'p', 'li']):
            # 图片处理力有未逮，暂不处理
            # if p.find("img"):
            #     # imgUrl = p.img.src.text
            #     img = p.img
            #     print(p)

            #容错
            if p.string == None or len(p.string) == 0:
                continue
            if p.name == 'p':
                if 'pw-post-body-paragraph' not in p['class']:
                    continue
                p.string += google_translate(p.string)
                text.append(Graphs.draw_text(p.string))
                if len(title) == 0:
                    title = p.string
            if p.name == 'h1':
                if len(title) > 0:
                    text.append(Graphs.draw_little_title(p.string))
                    text.append(Graphs.draw_little_title(google_translate(p.string)))
                else:
                    text.append(Graphs.draw_title(p.string))
                    text.append(Graphs.draw_title(google_translate(p.string)))
                    title = p.string
            if p.name == 'li':
                text.append(Graphs.draw_little_title(p.string))
                text.append(Graphs.draw_little_title(google_translate(p.string)))
            title = title.replace('?', '')
            title = title.replace('\'', '')
        doc = SimpleDocTemplate('./pdf/' + title + '.pdf', pagesize=A4)
        doc.build(text)
        title = ''
        text.clear()

            
        # elem = soup.find_all(['h1', 'p', 'li'])
        # for elm in elem:
        #     elmsoup = BeautifulSoup(str(elm), 'lxml')
        #     if p := elmsoup.html.body.find('p') != None:
        #         print(soup.find(elmsoup.html.body.p))
        #         if len(elmsoup.html.body.p.text) > 0:
        #             text = google_translate(elmsoup.html.body.p.text)
        #             elmsoup.html.body.p.append(text)
        #         print(elmsoup.html.body.p)
        #     # elif p := elmsoup.html.body.find('picture') != None:
        #     #     print("图片" + elmsoup.html.body.picture.text)
        #     elif p := elmsoup.html.body.find('h1') != None:
        #         if len(elmsoup.html.body.h1.text) > 0:
        #             text = google_translate(elmsoup.html.body.h1.text)
        #             elmsoup.html.body.h1.append(text)
        #         print(elmsoup.html.body.h1)
        #     else :
        #         text = google_translate(elmsoup.html.body.li.text)
        #         elmsoup.html.body.li.append(text)
        #         print(elmsoup.html.body.li)
        # print(title)

        # elem = soup1.find_all('p')
        # for m in elem:
        #     elmsoup = BeautifulSoup(str(m), 'lxml')
        #     if elmsoup.html.body.p.findChild('a') != None:
        #         print(elmsoup.html.body.p.a.text)
        #     elif elmsoup.html.body.p.has_attr('class'):
        #         attr = elmsoup.html.body.p['class']
        #         if 'pw-post-body-paragraph' in attr:
        #             print(elmsoup.html.body.p.text)
        # break


if __name__ == '__main__':
    res = findFirst10()
    contentList = retrieveFile(res)
    genPdf(contentList)

    #尝试直接用html转pdf，失败
    # config = pdfkit.configuration(wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    # pdfkit.from_file("modified.html", "modified.pdf")
