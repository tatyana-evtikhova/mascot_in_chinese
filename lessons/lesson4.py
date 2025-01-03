lesson = {
    'id': 4,
    'title': 'Time and Dates',
    'content': {
        'stages': [{
            'name': '⏰ Time Expressions',
            'type': 'learning',
            'title': 'Basic Time Expressions',
            'description': '''
Understanding time expressions is essential for daily communication in Chinese. From telling the time 
to discussing schedules, these phrases will help you navigate temporal conversations with confidence.
            ''',
            'content': '''
                <div class="learning-section">
                    <!-- Time of Day -->
                    <div class="main-expression" onclick="speakText('上午')">
                        <div class="expression-content">
                            <div class="chinese-text">上午</div>
                            <div class="expression-details">
                                <div class="pinyin">shàngwǔ</div>
                                <div class="meaning">morning</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('下午')">
                        <div class="expression-content">
                            <div class="chinese-text">下午</div>
                            <div class="expression-details">
                                <div class="pinyin">xiàwǔ</div>
                                <div class="meaning">afternoon</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('晚上')">
                        <div class="expression-content">
                            <div class="chinese-text">晚上</div>
                            <div class="expression-details">
                                <div class="pinyin">wǎnshang</div>
                                <div class="meaning">evening</div>
                            </div>
                        </div>
                    </div>

                    <!-- Time Units -->
                    <div class="main-expression" onclick="speakText('点')">
                        <div class="expression-content">
                            <div class="chinese-text">点</div>
                            <div class="expression-details">
                                <div class="pinyin">diǎn</div>
                                <div class="meaning">o'clock</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('分钟')">
                        <div class="expression-content">
                            <div class="chinese-text">分钟</div>
                            <div class="expression-details">
                                <div class="pinyin">fēnzhōng</div>
                                <div class="meaning">minute</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('半')">
                        <div class="expression-content">
                            <div class="chinese-text">半</div>
                            <div class="expression-details">
                                <div class="pinyin">bàn</div>
                                <div class="meaning">half</div>
                            </div>
                        </div>
                    </div>

                    <!-- Usage Notes -->
                    <div class="tone-rule">
                        <div class="rule-header">
                            <span class="rule-icon">💡</span>
                            <span class="rule-title">Time Format Rules</span>
                        </div>
                        <ul class="usage-notes">
                            <li>Hours always come before minutes: 三点十分 (3:10)</li>
                            <li>Use 半 for half past: 两点半 (2:30)</li>
                            <li>Quarter past/to uses 一刻: 三点一刻 (3:15)</li>
                            <li>AM/PM is indicated by 上午/下午 before the time</li>
                        </ul>
                    </div>

                    <!-- Common Usage -->
                    <div class="usage-examples">
                        <h4>Common Usage</h4>
                        <div class="usage-item" onclick="speakText('现在几点?')">
                            <div class="usage-chinese">现在几点?</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Xiànzài jǐ diǎn?</div>
                                <div class="usage-meaning">What time is it now?</div>
                            </div>
                        </div>
                        <div class="usage-item" onclick="speakText('上午八点半')">
                            <div class="usage-chinese">上午八点半</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Shàngwǔ bā diǎn bàn</div>
                                <div class="usage-meaning">8:30 AM</div>
                            </div>
                        </div>
                        <div class="usage-item" onclick="speakText('下午三点一刻')">
                            <div class="usage-chinese">下午三点一刻</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Xiàwǔ sān diǎn yī kè</div>
                                <div class="usage-meaning">3:15 PM</div>
                            </div>
                        </div>
                        <div class="usage-item" onclick="speakText('晚上十点')">
                            <div class="usage-chinese">晚上十点</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Wǎnshang shí diǎn</div>
                                <div class="usage-meaning">10:00 PM</div>
                            </div>
                        </div>
                    </div>
                </div>
            '''
        },
        {
            'name': '📅 Days and Dates',
            'type': 'learning',
            'title': 'Calendar Terms',
            'description': '''
Learning to talk about days, weeks, months, and years is crucial for daily life in Chinese. These terms 
will help you discuss schedules, make appointments, and talk about events in time.
            ''',
            'content': '''
                <div class="learning-section">
                    <!-- Days -->
                    <div class="main-expression" onclick="speakText('今天')">
                        <div class="expression-content">
                            <div class="chinese-text">今天</div>
                            <div class="expression-details">
                                <div class="pinyin">jīntiān</div>
                                <div class="meaning">today</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('明天')">
                        <div class="expression-content">
                            <div class="chinese-text">明天</div>
                            <div class="expression-details">
                                <div class="pinyin">míngtiān</div>
                                <div class="meaning">tomorrow</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('昨天')">
                        <div class="expression-content">
                            <div class="chinese-text">昨天</div>
                            <div class="expression-details">
                                <div class="pinyin">zuótiān</div>
                                <div class="meaning">yesterday</div>
                            </div>
                        </div>
                    </div>

                    <!-- Calendar Terms -->
                    <div class="main-expression" onclick="speakText('星期')">
                        <div class="expression-content">
                            <div class="chinese-text">星期</div>
                            <div class="expression-details">
                                <div class="pinyin">xīngqī</div>
                                <div class="meaning">week</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('月')">
                        <div class="expression-content">
                            <div class="chinese-text">月</div>
                            <div class="expression-details">
                                <div class="pinyin">yuè</div>
                                <div class="meaning">month</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('号')">
                        <div class="expression-content">
                            <div class="chinese-text">号</div>
                            <div class="expression-details">
                                <div class="pinyin">hào</div>
                                <div class="meaning">date (of month)</div>
                            </div>
                        </div>
                    </div>

                    <!-- Usage Notes -->
                    <div class="tone-rule">
                        <div class="rule-header">
                            <span class="rule-icon">💡</span>
                            <span class="rule-title">Date Format Rules</span>
                        </div>
                        <ul class="usage-notes">
                            <li>Year + Month + Date: 2024年一月一号</li>
                            <li>Days of week: 星期 + number (一 to 日)</li>
                            <li>Months: number + 月 (一月 to 十二月)</li>
                            <li>Dates: number + 号 (一号 to 三十一号)</li>
                        </ul>
                    </div>

                    <!-- Common Usage -->
                    <div class="usage-examples">
                        <h4>Common Usage</h4>
                        <div class="usage-item" onclick="speakText('今天星期几?')">
                            <div class="usage-chinese">今天星期几?</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Jīntiān xīngqī jǐ?</div>
                                <div class="usage-meaning">What day is it today?</div>
                            </div>
                        </div>
                        <div class="usage-item" onclick="speakText('明天见')">
                            <div class="usage-chinese">明天见</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Míngtiān jiàn</div>
                                <div class="usage-meaning">See you tomorrow</div>
                            </div>
                        </div>
                        <div class="usage-item" onclick="speakText('一月一号')">
                            <div class="usage-chinese">一月一号</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Yī yuè yī hào</div>
                                <div class="usage-meaning">January 1st</div>
                            </div>
                        </div>
                        <div class="usage-item" onclick="speakText('星期天')">
                            <div class="usage-chinese">星期天</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Xīngqītiān</div>
                                <div class="usage-meaning">Sunday</div>
                            </div>
                        </div>
                    </div>
                </div>
            '''
        }],
        'tips': '''
            <div class="notion-block">
                <div class="notion-callout">
                    <div class="notion-content">
                        <div class="notion-list">
                            <ul class="study-tips">
                                <li class="tip-item">
                                    <div class="tip-content">
                                        <h4>Time Structure</h4>
                                        <p>Learn the basic pattern: Number + 点 + Minutes</p>
                                    </div>
                                </li>
                                <li class="tip-item">
                                    <div class="tip-content">
                                        <h4>Date Order</h4>
                                        <p>Year → Month → Date: 2024年一月一号</p>
                                    </div>
                                </li>
                                <li class="tip-item">
                                    <div class="tip-content">
                                        <h4>Time Periods</h4>
                                        <p>Remember 上午 (morning), 下午 (afternoon), 晚上 (evening)</p>
                                    </div>
                                </li>
                                <li class="tip-item">
                                    <div class="tip-content">
                                        <h4>Common Questions</h4>
                                        <p>几点了? (What time is it?) 今天星期几? (What day is it?)</p>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        '''
    }
} 