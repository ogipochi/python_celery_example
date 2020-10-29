from celery import Celery

# Celeryオブジェクトを作成
app = Celery('proj',
             broker='redis://redis_app:6379/',
             backend='redis://redis_app:6379/',
             include=['proj.tasks'])

# タスクの結果の保持時間を変更
app.conf.update(
    result_expires=3600
)

if __name__ == '__main__':
    app.start()