lesson = {
    'id': 2,
    'title': 'Numbers 1-10',
    'icon': '/static/icons/number-10.png',
    'icon_credit': {
        'text': 'Number 10 icons created by Md Tanvirul Haque - Flaticon',
        'url': 'https://www.flaticon.com/free-icons/number-10'
    },
    'content': {
        'stages': [
            {
                'name': 'Basic Numbers',
                'type': 'learning',
                'icon': '🔢',
                'subtitle': 'Learn to count in Chinese',
                'content': '''
                <div class="learning-section">
                    <!-- Introduction -->
                    <div class="section-intro">
                        <p>Chinese numbers 1-10 are fundamental building blocks of the language. They are used frequently in daily life and form the basis for larger numbers.</p>
                    </div>

                    <!-- Main Numbers -->
                    <div class="main-expression" onclick="speakText('一')">
                        <div class="expression-content">
                            <div class="chinese-text">一</div>
                            <div class="expression-details">
                                <div class="pinyin">yī</div>
                                <div class="meaning">one (1)</div>
                            </div>
                        </div>
                        <div class="play-hint">Click to hear pronunciation</div>
                    </div>

                    <div class="main-expression" onclick="speakText('二')">
                        <div class="expression-content">
                            <div class="chinese-text">二</div>
                            <div class="expression-details">
                                <div class="pinyin">èr</div>
                                <div class="meaning">two (2)</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('三')">
                        <div class="expression-content">
                            <div class="chinese-text">三</div>
                            <div class="expression-details">
                                <div class="pinyin">sān</div>
                                <div class="meaning">three (3)</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('四')">
                        <div class="expression-content">
                            <div class="chinese-text">四</div>
                            <div class="expression-details">
                                <div class="pinyin">sì</div>
                                <div class="meaning">four (4)</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('五')">
                        <div class="expression-content">
                            <div class="chinese-text">五</div>
                            <div class="expression-details">
                                <div class="pinyin">wǔ</div>
                                <div class="meaning">five (5)</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('六')">
                        <div class="expression-content">
                            <div class="chinese-text">六</div>
                            <div class="expression-details">
                                <div class="pinyin">liù</div>
                                <div class="meaning">six (6)</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('七')">
                        <div class="expression-content">
                            <div class="chinese-text">七</div>
                            <div class="expression-details">
                                <div class="pinyin">qī</div>
                                <div class="meaning">seven (7)</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('八')">
                        <div class="expression-content">
                            <div class="chinese-text">八</div>
                            <div class="expression-details">
                                <div class="pinyin">bā</div>
                                <div class="meaning">eight (8)</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('九')">
                        <div class="expression-content">
                            <div class="chinese-text">九</div>
                            <div class="expression-details">
                                <div class="pinyin">jiǔ</div>
                                <div class="meaning">nine (9)</div>
                            </div>
                        </div>
                    </div>

                    <div class="main-expression" onclick="speakText('十')">
                        <div class="expression-content">
                            <div class="chinese-text">十</div>
                            <div class="expression-details">
                                <div class="pinyin">shí</div>
                                <div class="meaning">ten (10)</div>
                            </div>
                        </div>
                    </div>

                    <!-- Important Notes -->
                    <div class="tone-rule">
                        <div class="rule-header">
                            <span class="rule-icon">💡</span>
                            <span class="rule-title">Important Notes</span>
                        </div>
                        <ul class="usage-notes">
                            <li>The first three numbers (一, 二, 三) are written as horizontal lines</li>
                            <li>二 (èr) becomes 两 (liǎng) when counting objects</li>
                            <li>四 (4) is considered unlucky as it sounds similar to 死 (sǐ, death)</li>
                            <li>八 (8) is considered lucky as it sounds similar to 发 (fā, prosperity)</li>
                        </ul>
                    </div>

                    <!-- Usage Examples -->
                    <div class="usage-examples">
                        <h4>Common Usage</h4>
                        
                        <div class="usage-item" onclick="speakText('一个人')">
                            <div class="usage-chinese">一个人</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">yí ge rén</div>
                                <div class="usage-meaning">one person</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('两本书')">
                            <div class="usage-chinese">两本书</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">liǎng běn shū</div>
                                <div class="usage-meaning">two books</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('三点钟')">
                            <div class="usage-chinese">三点钟</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">sān diǎn zhōng</div>
                                <div class="usage-meaning">three o'clock</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('五分钟')">
                            <div class="usage-chinese">五分钟</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǔ fēn zhōng</div>
                                <div class="usage-meaning">five minutes</div>
                            </div>
                        </div>
                    </div>
                </div>
                '''
            }
        ],
        'tips': '''
        <div class="notion-block">
            <div class="notion-callout">
                <div class="notion-content">
                    <div class="notion-list">
                    <ul class="study-tips">
                        <li class="tip-item">
                            <div class="tip-content">
                                <h4>Writing Practice</h4>
                                <p>Practice writing numbers in the correct stroke order, starting with simple ones (一, 二, 三)</p>
                            </div>
                        </li>
                        <li class="tip-item">
                            <div class="tip-content">
                                <h4>Counting Practice</h4>
                                <p>Count objects around you in Chinese to reinforce number usage</p>
                            </div>
                        </li>
                        <li class="tip-item">
                            <div class="tip-content">
                                <h4>Measure Words</h4>
                                <p>Learn common measure words used with numbers (个, 本, 张)</p>
                            </div>
                        </li>
                        <li class="tip-item">
                            <div class="tip-content">
                                <h4>Tone Practice</h4>
                                <p>Pay attention to tone changes, especially with 一 (yī)</p>
                            </div>
                        </li>
                    </ul>
                    </div>
                </div>
            </div>
        </div>
        ''',
        'mistakes': '''
        <div class="notion-block">
            <div class="notion-callout warning">
                <div class="notion-icon">⚠️</div>
                <div class="notion-content">
                    <div class="notion-title">Common Mistakes to Avoid</div>
                    <div class="notion-list">
                    <ul class="common-mistakes">
                        <li>Don't forget to use 两 (liǎng) instead of 二 (èr) when counting objects</li>
                        <li>Watch out for tone changes with 一 (yī)</li>
                        <li>Remember to use measure words with numbers</li>
                        <li>Pay attention to stroke order when writing numbers</li>
                    </ul>
                    </div>
                </div>
            </div>
        </div>
        '''
    }
} 