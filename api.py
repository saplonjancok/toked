from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/config', methods=['GET'])
def get_config():
    config = {
        "url": "https://api22-normal-c-useast1a.tiktokv.com/lite/v2/comment/publication/?manifest_version_code=350801&_rticket=1729607395606&app_language=id&app_type=normal&iid=7428606856031749894&channel=googleplay&device_type=SM-G965F&language=id&host_abi=arm64-v8a&locale=id-ID&resolution=1080*2094&openudid=53b7be8aa7bd3ae1&update_version_code=350801&ac2=wifi5g&cdid=4219f665-936d-49a1-a170-6150d5a7fe42&sys_region=ID&os_api=29&timezone_name=Asia%2FSeoul&dpi=420&ac=wifi&device_id=7428602535186056709&os_version=10&timezone_offset=32400&version_code=350801&app_name=musically_go&ab_version=35.8.1&version_name=35.8.1&device_brand=samsung&op_region=ID&ssmix=a&device_platform=android&build_number=35.8.1&region=ID&aid=1340&ts=1729607337",
        "headers": {
            'accept-encoding': 'ttzip',
            'connection': 'Keep-Alive',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'store-idc=maliva; ...',
            'host': 'api22-normal-c-useast1a.tiktokv.com',
            'passport-sdk-version': '30990',
            'sdk-version': '2',
            'user-agent': 'com.zhiliaoapp.musically.go/350801 ...',
            'x-argus': 'xf8ks09irUSrNq+bgYFwHCRUCNhcEVaaY2aifO3/X616E4UOtGqhaC76S0POFih8uRsUySQ5TvLjfAUsSZIFUUawWqXmCW1i9vz+QScZ1MP3ujOpv++ulQ1jW0c05RYxicev2p7aIEvbkfCMelfzdRAfavgzOWcnvM23z2peZ+K8FVj7d6pxx4rh10YhzF8Bf22ZPnGAWRNBo7nNrUvLsgmms/fhlPbPPfSH+XIyJYt78FLhG/tH8w/uh5ZsG+GR8br01WUMbXxpyewxvMxWi1B2KV0efUn/Fzv3YfkbLvWVA/9RYIZhhrzY2Sig7SaMtcONLcZ3bOGFisstMxe8lhGLxtV5nz1Or/lPsbKN1ryJRVBKPTP8IasG9I/L+b7jxcQQtWUOk3treOD4dCjYyXMfmQSLXyQPCYFPvU7/qxMjOJaDENe1hEn7yIZrTVBUfbXL259upc5rSsiYizWKANburyK1PviLv8hIDZh1S388IZ8/UFF9U0K294WIeQnIBTgyzgwy9w1hI8ynWgUD/llDoEzSBBEsDwhKeCIabx+mXQ==',
            'x-gorgon': '840440a80001b2a9a3b78430b0fa3670527af00c7ded3ba610ed',
            'x-khronos': '1729607395',
            'x-ladon': 'TJYfLtPfDV7ZvcZ3klpPiJnwNdvML4EjB2dcY1eFl3T6ino7',
            'x-ss-stub': '91546561CA59AA73AD91EE90963C7849',
            'x-tt-req-timeout': '90000',
            'x-tt-store-region': 'id',
            'x-tt-store-region-src': 'uid',
            'x-tt-token': 'token',  # This should be replaced dynamically
            'x-tt-ultra-lite': '1',
            'x-vc-bdturing-sdk-version': '2.3.2.i18n'
        }
    }
    return jsonify(config)

if __name__ == '__main__':
    app.run()
