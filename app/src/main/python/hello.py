from android.os import Bundle
from androidx.appcompat.app import AppCompatActivity
from com.chaquo.python.hello import R
from java import jvoid, Override, static_proxy

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World!"


class MainActivity(static_proxy(AppCompatActivity)):

    @Override(jvoid, [Bundle])
    def onCreate(self, state):
        AppCompatActivity.onCreate(self, state)
        self.setContentView(R.layout.activity_main)
        app.run()

