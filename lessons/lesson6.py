lesson = {
    'id': 6,
    'title': 'Action Verbs',
    'title_en': 'Action Verbs',
    'icon': '🎯',  # Using emoji as icon until we have a custom one
    'content': {
        'description': '''
            In this lesson, we'll learn common Chinese action verbs.
            These verbs are essential for describing daily activities.
        ''',
        'stages': [
            {
                'name': 'Basic Verbs',
                'type': 'learning',
                'icon': '🎯',
                'subtitle': 'Learn essential Chinese verbs',
    'content': '''
                    <div class="learning-section">
                        <div class="section-intro">
                            <p>Chinese verbs are simpler than English verbs - they don't change form for tense or person. 
                            Learning these basic verbs will help you construct simple sentences and express daily actions.</p>
                        </div>

                        <!-- Basic Verbs -->
                        <div class="main-expression" onclick="speakText('是')">
                            <div class="expression-content">
                                <div class="chinese-text">是</div>
                                <div class="expression-details">
                                    <div class="pinyin">shì</div>
                                    <div class="meaning">to be</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('有')">
                            <div class="expression-content">
                                <div class="chinese-text">有</div>
                                <div class="expression-details">
                                    <div class="pinyin">yǒu</div>
                                    <div class="meaning">to have</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('在')">
                            <div class="expression-content">
                                <div class="chinese-text">在</div>
                                <div class="expression-details">
                                    <div class="pinyin">zài</div>
                                    <div class="meaning">to be at/in</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('去')">
                            <div class="expression-content">
                                <div class="chinese-text">去</div>
                                <div class="expression-details">
                                    <div class="pinyin">qù</div>
                                    <div class="meaning">to go</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('要')">
                            <div class="expression-content">
                                <div class="chinese-text">要</div>
                                <div class="expression-details">
                                    <div class="pinyin">yào</div>
                                    <div class="meaning">to want/will</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('想')">
                            <div class="expression-content">
                                <div class="chinese-text">想</div>
                                <div class="expression-details">
                                    <div class="pinyin">xiǎng</div>
                                    <div class="meaning">to want/to think</div>
                                </div>
                            </div>
                        </div>

                        <!-- Daily Action Verbs -->
                        <div class="main-expression" onclick="speakText('吃')">
                            <div class="expression-content">
                                <div class="chinese-text">吃</div>
                                <div class="expression-details">
                                    <div class="pinyin">chī</div>
                                    <div class="meaning">to eat</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('喝')">
                            <div class="expression-content">
                                <div class="chinese-text">喝</div>
                                <div class="expression-details">
                                    <div class="pinyin">hē</div>
                                    <div class="meaning">to drink</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('说')">
                            <div class="expression-content">
                                <div class="chinese-text">说</div>
                                <div class="expression-details">
                                    <div class="pinyin">shuō</div>
                                    <div class="meaning">to speak/say</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('看')">
                            <div class="expression-content">
                                <div class="chinese-text">看</div>
                                <div class="expression-details">
                                    <div class="pinyin">kàn</div>
                                    <div class="meaning">to look/watch</div>
                                </div>
                            </div>
                        </div>

                        <!-- Activity Verbs -->
                        <div class="main-expression" onclick="speakText('学习')">
                            <div class="expression-content">
                                <div class="chinese-text">学习</div>
                                <div class="expression-details">
                                    <div class="pinyin">xuéxí</div>
                                    <div class="meaning">to study</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('工作')">
                            <div class="expression-content">
                                <div class="chinese-text">工作</div>
                                <div class="expression-details">
                                    <div class="pinyin">gōngzuò</div>
                                    <div class="meaning">to work</div>
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
                                <li>Chinese verbs don't change form for tense</li>
                                <li>No conjugation needed for different persons</li>
                                <li>Time words come before verbs</li>
                                <li>Location words come after verbs</li>
                            </ul>
                        </div>

                        <!-- Additional Grammar Notes -->
                        <div class="tone-rule">
                            <div class="rule-header">
                                <span class="rule-icon">📝</span>
                                <span class="rule-title">Grammar Notes</span>
                            </div>
                            <ul class="usage-notes">
                                <li>Verb + 了 indicates completed action</li>
                                <li>要/想 + Verb expresses desire or intention</li>
                                <li>会 + Verb indicates ability or skill</li>
                                <li>能 + Verb indicates possibility or permission</li>
                            </ul>
                        </div>

                        <!-- Usage Note for Want -->
                        <div class="tone-rule">
                            <div class="rule-header">
                                <span class="rule-icon">💡</span>
                                <span class="rule-title">Want: 要 vs 想</span>
                            </div>
                            <ul class="usage-notes">
                                <li>要 (yào) is more immediate or certain</li>
                                <li>想 (xiǎng) is more of a desire or wish</li>
                                <li>Both are followed directly by verbs</li>
                                <li>Use 想要 for "want to have" something</li>
                            </ul>
                        </div>
                    </div>
                '''
            },
            {
                'name': 'Common Usage',
                'type': 'examples',
                'content': '''
                    <div class="usage-examples">
                        <!-- Basic Sentences -->
                        <div class="usage-item" onclick="speakText('我是学生')">
                            <div class="usage-chinese">我是学生</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ shì xuéshēng</div>
                                <div class="usage-meaning">I am a student</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('我有一本书')">
                            <div class="usage-chinese">我有一本书</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ yǒu yì běn shū</div>
                                <div class="usage-meaning">I have a book</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('他在家')">
                            <div class="usage-chinese">他在家</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">tā zài jiā</div>
                                <div class="usage-meaning">He is at home</div>
                            </div>
                        </div>

                        <!-- Action Verbs -->
                        <div class="usage-item" onclick="speakText('我去学校')">
                            <div class="usage-chinese">我去学校</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ qù xuéxiào</div>
                                <div class="usage-meaning">I go to school</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('我想吃饭')">
                            <div class="usage-chinese">我想吃饭</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ xiǎng chī fàn</div>
                                <div class="usage-meaning">I want to eat</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('他会说中文')">
                            <div class="usage-chinese">他会说中文</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">tā huì shuō zhōngwén</div>
                                <div class="usage-meaning">He can speak Chinese</div>
                            </div>
                        </div>

                        <!-- Complex Examples -->
                        <div class="usage-item" onclick="speakText('我要去工作了')">
                            <div class="usage-chinese">我要去工作了</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ yào qù gōngzuò le</div>
                                <div class="usage-meaning">I'm going to work</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('你能看见吗')">
                            <div class="usage-chinese">你能看见吗</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">nǐ néng kànjiàn ma</div>
                                <div class="usage-meaning">Can you see?</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('我学习了三个小时')">
                            <div class="usage-chinese">我学习了三个小时</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ xuéxí le sān ge xiǎoshí</div>
                                <div class="usage-meaning">I studied for three hours</div>
                            </div>
                        </div>

                        <!-- Want/Desire Examples -->
                        <div class="usage-item" onclick="speakText('我要回家')">
                            <div class="usage-chinese">我要回家</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ yào huí jiā</div>
                                <div class="usage-meaning">I will go home</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('我想学中文')">
                            <div class="usage-chinese">我想学中文</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ xiǎng xué zhōngwén</div>
                                <div class="usage-meaning">I want to learn Chinese</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('我想要那本书')">
                            <div class="usage-chinese">我想要那本书</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ xiǎng yào nà běn shū</div>
                                <div class="usage-meaning">I want that book</div>
                            </div>
                        </div>
                    </div>
                '''
            }
        ],
    'tips': '''
            <div class="study-tips">
                <div class="section-title">
                    <div class="title-with-icon">
                        <span class="icon">💡</span>
                        <span>Study Tips</span>
                    </div>
                </div>
                <div class="tip-block">
                    <h4>Basic Structure</h4>
                    <p>Subject + Verb + Object (我去学校)</p>
                </div>

                <div class="tip-block">
                    <h4>Time Words</h4>
                    <p>Place time words before the verb (明天去)</p>
                </div>

                <div class="tip-block">
                    <h4>Location Words</h4>
                    <p>Place location words after the verb (去学校)</p>
                </div>

                <div class="tip-block">
                    <h4>Verb Combinations</h4>
                    <p>Learn common verb pairs (去吃饭 - go eat)</p>
                </div>
            </div>
''',
    'mistakes': '''
            <div class="study-tips warning">
                <div class="tip-block">
                    <h4>Verb Forms</h4>
                    <p>Don't add -ing or -ed endings to verbs</p>
                </div>

                <div class="tip-block">
                    <h4>Word Order</h4>
                    <p>Don't put time words after the verb</p>
                </div>

                <div class="tip-block">
                    <h4>Verb Usage</h4>
                    <p>Don't use 是 for locations (use 在 instead)</p>
                </div>

                <div class="tip-block">
                    <h4>Object Position</h4>
                    <p>Don't forget the object after transitive verbs</p>
                </div>
            </div>
        '''
    }
} 